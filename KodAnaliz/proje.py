from tkinter import Tk, Label, Button, messagebox

# Şartname Ekranı
def sartname_ekrani():
    sartname_penceresi = Tk()
    sartname_penceresi.title("Yazılım Kullanım Şartnamesi")
    sartname_penceresi.geometry("800x400")
    sartname_penceresi.configure(bg="#f0f4f7")

    sartname_metni = """ Yazılım Kalite ve Analiz Projesi Kullanım ve Uyarlama Sözleşmesi

1. TARAFLAR
Bu sözleşme, T.C. Üniversitesi ve Proje Geliştirme Ekibi arasında imzalanmıştır.

2. TANIMLAR
Yazılım Kalite ve Analiz Projesi: Kod benzerlik oranı, metrik üretimi, güvenlik analizi gibi özellikler içeren bir yazılım.

3. UYARLAMA VE KURULUM
Proje, Üniversite tarafından sağlanan ihtiyaçlara göre uyarlanacaktır.

4. EĞİTİM
Kullanıcılara yazılımın kullanımı için eğitim sağlanacaktır.

5. GİZLİLİK
Tüm bilgiler gizli tutulacak ve tarafların onayı olmadan paylaşılmayacaktır.

6. FESİH
Taraflardan birinin yükümlülüklerini yerine getirmemesi durumunda sözleşme feshedilebilir.

7. ANLAŞMAZLIK
Anlaşmazlık durumunda İzmir Mahkemeleri yetkilidir.   
    """
    
    Label(sartname_penceresi, text=sartname_metni, font=("Arial", 12), bg="#f0f4f7", wraplength=750, justify="left").pack(padx=10, pady=10)

    def kabul_et():
        sartname_penceresi.destroy()
        main_program()  # Ana programa geçiş

    def reddet():
        sartname_penceresi.destroy()
        messagebox.showinfo("Şartname Reddedildi", "Şartname reddedildi. Program sonlanıyor.")
        exit()

    Button(sartname_penceresi, text="Kabul Ediyorum", command=kabul_et, font=("Arial", 12), bg="#0078d7", fg="white").pack(side="left", padx=20, pady=20)
    Button(sartname_penceresi, text="Reddet", command=reddet, font=("Arial", 12), bg="#d9534f", fg="white").pack(side="right", padx=20, pady=20)

    sartname_penceresi.mainloop()

# Program Giriş Noktası
if __name__ == "__main__":
    sartname_ekrani()



import os
import ast
import subprocess
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from graphviz import Digraph
from radon.metrics import mi_parameters
from radon.complexity import cc_visit
from radon.raw import analyze
import coverage
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from tkinter import Tk, Label, Button, Text, Scrollbar, END, Frame, filedialog

# 1. Kod Benzerlik Analizi
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

def kod_benzerlik_hesapla(kod1: str, kod2: str) -> dict:
    if not kod1 or not kod2:
        raise ValueError("Kodlar boş olamaz.")

    # 1. Token Benzerliği
    vectorizer = CountVectorizer().fit_transform([kod1, kod2])
    token_benzerlik = cosine_similarity(vectorizer)[0][1]

    # Yardımcı Fonksiyonlar
    def agac_vektor(agac):
        return [type(node)._name_ for node in ast.walk(ast.parse(agac))]

    def metinleri_ayristir(kod, tip):
        if tip == ast.Name:
            return [n.id for n in ast.walk(ast.parse(kod)) if isinstance(n, ast.Name)]
        elif tip == ast.FunctionDef:
            return [n.name for n in ast.walk(ast.parse(kod)) if isinstance(n, ast.FunctionDef)]
        elif tip == ast.ClassDef:
            return [n.name for n in ast.walk(ast.parse(kod)) if isinstance(n, ast.ClassDef)]
        else:
            return []

    # 2. Yapısal Benzerlik
    agac_kod1 = agac_vektor(kod1)
    agac_kod2 = agac_vektor(kod2)
    yapisal_benzerlik = len(set(agac_kod1).intersection(agac_kod2)) / len(set(agac_kod1 + agac_kod2))

    # 3. Değişken Adları Benzerliği
    degisken_benzerlik = len(set(metinleri_ayristir(kod1, ast.Name)).intersection(metinleri_ayristir(kod2, ast.Name))) / max(len(set(metinleri_ayristir(kod1, ast.Name)) | set(metinleri_ayristir(kod2, ast.Name))), 1)

    # 4. Fonksiyon Adları Benzerliği
    fonksiyon_benzerlik = len(set(metinleri_ayristir(kod1, ast.FunctionDef)).intersection(metinleri_ayristir(kod2, ast.FunctionDef))) / max(len(set(metinleri_ayristir(kod1, ast.FunctionDef)) | set(metinleri_ayristir(kod2, ast.FunctionDef))), 1)

    # 5. Sınıf Adları Benzerliği
    sinif_benzerlik = len(set(metinleri_ayristir(kod1, ast.ClassDef)).intersection(metinleri_ayristir(kod2, ast.ClassDef))) / max(len(set(metinleri_ayristir(kod1, ast.ClassDef)) | set(metinleri_ayristir(kod2, ast.ClassDef))), 1)

    # 6. Modül Benzerliği
    moduller = lambda kod: [n.names[0].name for n in ast.walk(ast.parse(kod)) if isinstance(n, ast.Import)]
    modul_benzerlik = len(set(moduller(kod1)).intersection(set(moduller(kod2)))) / max(len(set(moduller(kod1)) | set(moduller(kod2))), 1)

    # 7. String Benzerliği
    string_benzerlik = len(set([n.value for n in ast.walk(ast.parse(kod1)) if isinstance(n, ast.Constant) and isinstance(n.value, str)]).intersection(
        [n.value for n in ast.walk(ast.parse(kod2)) if isinstance(n, ast.Constant) and isinstance(n.value, str)])) / max(len(set([n.value for n in ast.walk(ast.parse(kod1)) if isinstance(n, ast.Constant) and isinstance(n.value, str)]).union(
        [n.value for n in ast.walk(ast.parse(kod2)) if isinstance(n, ast.Constant) and isinstance(n.value, str)])), 1)

    # 8. Yorum Satırları Benzerliği
    def yorumlari_ayristir(kod):
        return [line.strip() for line in kod.split('\n') if line.strip().startswith('#')]

    yorum_benzerlik = len(set(yorumlari_ayristir(kod1)).intersection(set(yorumlari_ayristir(kod2)))) / max(len(set(yorumlari_ayristir(kod1)).union(set(yorumlari_ayristir(kod2)))), 1)

    # 9. Döngü Türleri Benzerliği
    def dongu_sayisi(kod):
        return len([node for node in ast.walk(ast.parse(kod)) if isinstance(node, (ast.For, ast.While))])

    dongu_benzerlik = min(dongu_sayisi(kod1), dongu_sayisi(kod2)) / max(dongu_sayisi(kod1), dongu_sayisi(kod2)) if max(dongu_sayisi(kod1), dongu_sayisi(kod2)) > 0 else 0

    # 10. Koşul Yapıları Benzerliği
    def kosul_sayisi(kod):
        return len([node for node in ast.walk(ast.parse(kod)) if isinstance(node, ast.If)])

    kosul_benzerlik = min(kosul_sayisi(kod1), kosul_sayisi(kod2)) / max(kosul_sayisi(kod1), kosul_sayisi(kod2)) if max(kosul_sayisi(kod1), kosul_sayisi(kod2)) > 0 else 0

    return {
        "Token Benzerliği": token_benzerlik * 100,
        "Yapısal Benzerlik": yapisal_benzerlik * 100,
        "Değişken Adları Benzerliği": degisken_benzerlik * 100,
        "Fonksiyon Adları Benzerliği": fonksiyon_benzerlik * 100,
        "Sınıf Adları Benzerliği": sinif_benzerlik * 100,
        "Modül Benzerliği": modul_benzerlik * 100,
        "String Benzerliği": string_benzerlik * 100,
        "Yorum Satırları Benzerliği": yorum_benzerlik * 100,
        "Döngü Türleri Benzerliği": dongu_benzerlik * 100,
        "Koşul Yapıları Benzerliği": kosul_benzerlik * 100
    }

# 2. Kodun Graph Gösterimi
def kodu_graf_olustur(kod: str, baslik: str):
    agac = ast.parse(kod)
    graph = Digraph(comment=baslik)

    for node in ast.walk(agac):
        node_id = id(node)
        graph.node(str(node_id), type(node)._name_)
        for child in ast.iter_child_nodes(node):
            graph.edge(str(node_id), str(id(child)))

    try:
        graph.render(f"{baslik}_graph", format="png", cleanup=True)
        img = plt.imread(f"{baslik}_graph.png")
        plt.figure(figsize=(12, 8))
        plt.imshow(img)
        plt.axis('off')
        plt.title(f"{baslik} Graph Gösterimi", fontsize=20)
        plt.show()
    except FileNotFoundError:
        print("Graphviz dot executable bulunamadı. Lütfen Graphviz'in kurulu ve PATH'e ekli olduğundan emin olun.")

# 3. Metrik Analizi
def metrik_uret(kod: str) -> dict:
    karmaşıklık = cc_visit(kod)
    raw_metrics = analyze(kod)
    parametreler = mi_parameters(kod)

    return {
        "Karmaşıklık Seviyesi": len(karmaşıklık),
        "Toplam Satır": raw_metrics.loc,
        "Boş Satır": raw_metrics.lloc,
        "Yorum Satırı": raw_metrics.comments,
        "Fonksiyon Sayısı": len([n for n in ast.walk(ast.parse(kod)) if isinstance(n, ast.FunctionDef)]),
        "Değişken Sayısı": len([n for n in ast.walk(ast.parse(kod)) if isinstance(n, ast.Name)]),
        "Import Sayısı": len([n for n in ast.walk(ast.parse(kod)) if isinstance(n, ast.Import)]),
        "Yorum Oranı": raw_metrics.comments / raw_metrics.loc * 100 if raw_metrics.loc else 0,
        "Kod Satırı Oranı": raw_metrics.lloc / raw_metrics.loc * 100 if raw_metrics.loc else 0,
        "Karmaşıklık Ortalama": np.mean([n.complexity for n in karmaşıklık]) if karmaşıklık else 0
    }

# 4. Kod Koku Analizi
def kod_kokularini_tespit_et(kod: str) -> list:
    kokular = []

    for node in ast.walk(ast.parse(kod)):
        # 1. Çok Uzun Fonksiyon
        if isinstance(node, ast.FunctionDef) and len(node.body) > 30:
            kokular.append(f"Fonksiyon {node.name} çok uzun ({len(node.body)} satır)")

        # 2. Uzun Parametre Listesi
        if isinstance(node, ast.FunctionDef) and len(node.args.args) > 5:
            kokular.append(f"Fonksiyon {node.name} çok fazla parametre alıyor ({len(node.args.args)} parametre)")

        # 3. Ölü Kod
        if isinstance(node, ast.FunctionDef) and not any(
            isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == node.name
            for n in ast.walk(ast.parse(kod))
        ):
            kokular.append(f"Fonksiyon {node.name} kullanılmıyor (ölü kod)")

        # 4. Tekrar Eden Kod
        if isinstance(node, ast.Assign) and any(
            n for n in ast.walk(ast.parse(kod)) if isinstance(n, ast.Assign) and n != node and ast.dump(n) == ast.dump(node)
        ):
            kokular.append("Tekrar eden kod bloğu tespit edildi")

        # 5. Büyük Sınıf
        if isinstance(node, ast.ClassDef) and len(node.body) > 100:
            kokular.append(f"Çok büyük sınıf: {node.name} ({len(node.body)} satır)")

        # 6. Fazla Modül Bağımlılığı
        if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
            kokular.append(f"Modül içe aktarıldı: {node.names[0].name}")

        # 7. Derin İf-Else Zinciri
        if isinstance(node, ast.If):
            depth = 0
            while isinstance(node, ast.If):
                depth += 1
                node = node.body[0] if node.body else None
            if depth > 4:
                kokular.append(f"Derin if-else zinciri tespit edildi ({depth} seviye)")

        # 8. Yetersiz Hata Yönetimi
        if isinstance(node, ast.FunctionDef) and not any(isinstance(n, ast.Try) for n in node.body):
            kokular.append(f"Fonksiyon {node.name} hata yönetimi içermiyor")

        # 9. Çok Fazla Döngü
        if isinstance(node, (ast.For, ast.While)):
            kokular.append("Döngü tespit edildi")

        # 10. Magic Numbers
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and node.value not in [0, 1, -1]:
            kokular.append(f"Magic number kullanımı: {node.value}")

    return kokular



# 5. Cover Oranı Hesaplaması
def cover_orani_hesapla(proje_kod: str, test_kod: str) -> dict:
    with open("proje_kod.py", "w") as f:
        f.write(proje_kod)
    with open("test_kod.py", "w") as f:
        f.write(test_kod)

    cov = coverage.Coverage(source=["proje_kod"])
    cov.start()

    try:
        exec(test_kod)
    except Exception as e:
        print(f"Test kodu çalıştırılırken hata oluştu: {e}")

    cov.stop()
    cov.save()

    try:
        report = cov.report()
    except coverage.exceptions.NoDataError:
        report = 0

    cov.erase()
    os.remove("proje_kod.py")
    os.remove("test_kod.py")

    return {"Cover Oranı": report}

# Güvenlik ve Hata Analizi
def kod_guvenligi_ve_hata_tahmini(kod: str) -> list:
    issues = []
    for node in ast.walk(ast.parse(kod)):
        if isinstance(node, ast.Try):
            issues.append("Try-Except Bloğu Kullanılmış")
        elif isinstance(node, ast.Import):
            issues.append(f"Modül İçe Aktarımı: {node.names[0].name}")
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in ['eval', 'exec']:
                issues.append(f"Tehlikeli Fonksiyon Kullanımı: {node.func.id}")
        elif isinstance(node, ast.FunctionDef) and "password" in [arg.arg.lower() for arg in node.args.args]:
            issues.append(f"Fonksiyon {node.name} şifre parametresi içeriyor.")
        elif isinstance(node, ast.With):
            issues.append("With bloğu kullanımı, kaynak yönetimi kontrol edilmeli.")
    return issues

# Görselleştirme Fonksiyonları
def grafik_ciz(labels, values, title, xlabel, ylabel, palette="Blues_d"):
    plt.figure(figsize=(12, 8))
    sns.barplot(x=labels, y=values, palette=palette)
    plt.title(title, fontsize=20)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.tight_layout()
    plt.show()

def kod_koku_gorsellestir(kokular: list):
    # Kokuların kategorize edilmesi
    kokular_kategorize = {}
    for koku in kokular:
        kategori = koku.split("(")[0].strip()
        kokular_kategorize[kategori] = kokular_kategorize.get(kategori, 0) + 1

    labels = list(kokular_kategorize.keys())
    values = list(kokular_kategorize.values())

    plt.figure(figsize=(16, 10))  # Grafik boyutu artırıldı
    sns.barplot(x=labels, y=values, palette="coolwarm")
    
    # Çubuklar üzerine değerler ekleniyor
    for i, value in enumerate(values):
        plt.text(i, value + 0.1, f"{value:.0f}", ha="center", fontsize=14, color="black")  # Değerlerin hizası

    plt.title("Kod Koku Analizi", fontsize=24)  # Başlık boyutu artırıldı
    plt.xlabel("Kod Koku Türleri", fontsize=18)  # X ekseni etiketi boyutu artırıldı
    plt.ylabel("Frekans", fontsize=18)  # Y ekseni etiketi boyutu artırıldı
    plt.xticks(rotation=45, fontsize=14)  # X ekseni değer boyutu artırıldı
    plt.yticks(fontsize=14)  # Y ekseni değer boyutu artırıldı
    plt.tight_layout()  # Çakışmayı engellemek için
    plt.show()




def cover_orani_gorsellestir(oran: float):
    labels = ["Kaplanan Kısım", "Kaplanmayan Kısım"]
    values = [oran, 100 - oran]

    plt.figure(figsize=(8, 8))
    plt.bar(labels, values, color=["green", "gray"])
    plt.title("Kod Cover Oranı", fontsize=20)
    plt.ylabel("Oran (%)", fontsize=14)
    plt.show()

# Kullanıcı Arayüzü
def arayuz_baslat():
    arayuz = Tk()
    arayuz.title("Kod Analiz Aracı")
    arayuz.geometry("800x600")
    arayuz.configure(bg="#f0f4f7")

    frame = Frame(arayuz, bg="#f0f4f7")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    Label(frame, text="Kod-1'inizi aşağıya yapıştırınız:", font=("Arial", 14), bg="#f0f4f7").grid(row=0, column=0, sticky="w")
    metin_alani1 = Text(frame, wrap='word', height=10, font=("Arial", 12), bg="#ffffff", fg="#000000")
    metin_alani1.grid(row=1, column=0, sticky="nsew")

    Label(frame, text="Kod-2'nizi aşağıya yapıştırınız:", font=("Arial", 14), bg="#f0f4f7").grid(row=2, column=0, sticky="w")
    metin_alani2 = Text(frame, wrap='word', height=10, font=("Arial", 12), bg="#ffffff", fg="#000000")
    metin_alani2.grid(row=3, column=0, sticky="nsew")

    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(3, weight=1)

    def benzerlik_analiz():
        kod1 = metin_alani1.get("1.0", END).strip()
        kod2 = metin_alani2.get("1.0", END).strip()
        if kod1 and kod2:
            benzerlik = kod_benzerlik_hesapla(kod1, kod2)
            grafik_ciz(list(benzerlik.keys()), list(benzerlik.values()), "Kod Benzerlik Analizi", "Kriterler", "Benzerlik (%)")

    def graph_analiz():
        kod1 = metin_alani1.get("1.0", END).strip()
        if kod1:
            kodu_graf_olustur(kod1, "Kod-1")

    def metrik_analiz():
        kod1 = metin_alani1.get("1.0", END).strip()
        if kod1:
            metrikler1 = metrik_uret(kod1)
            grafik_ciz(list(metrikler1.keys()), list(metrikler1.values()), "Kod Metrikleri", "Metrikler", "Değerler")

    def kod_koku_analiz():
        kod1 = metin_alani1.get("1.0", END).strip()
        if kod1:
            kokular1 = kod_kokularini_tespit_et(kod1)
            kod_koku_gorsellestir(kokular1)

    def cover_analiz():
        kod1 = metin_alani1.get("1.0", END).strip()
        kod2 = metin_alani2.get("1.0", END).strip()
        if kod1 and kod2:
            cover_orani = cover_orani_hesapla(kod1, kod2)["Cover Oranı"]
            cover_orani_gorsellestir(cover_orani)

    def guvenlik_analiz():
        kod1 = metin_alani1.get("1.0", END).strip()
        kod2 = metin_alani2.get("1.0", END).strip()
        results = {}
        if kod1:
            results["Kod-1"] = kod_guvenligi_ve_hata_tahmini(kod1)
        if kod2:
            results["Kod-2"] = kod_guvenligi_ve_hata_tahmini(kod2)

        if results:
            output = "".join([f"{key}: " + "\n".join(val) + "\n\n" for key, val in results.items()])
            print(output)

    Button(frame, text="Benzerlik Analizi", command=benzerlik_analiz, font=("Arial", 12), bg="#0078d7", fg="#ffffff", activebackground="#005a9e", activeforeground="#ffffff").grid(row=4, column=0, pady=5, sticky="ew")
    Button(frame, text="Graph Analizi", command=graph_analiz, font=("Arial", 12), bg="#0078d7", fg="#ffffff", activebackground="#005a9e", activeforeground="#ffffff").grid(row=5, column=0, pady=5, sticky="ew")
    Button(frame, text="Metrik Analizi", command=metrik_analiz, font=("Arial", 12), bg="#0078d7", fg="#ffffff", activebackground="#005a9e", activeforeground="#ffffff").grid(row=6, column=0, pady=5, sticky="ew")
    Button(frame, text="Kod Koku Analizi", command=kod_koku_analiz, font=("Arial", 12), bg="#0078d7", fg="#ffffff", activebackground="#005a9e", activeforeground="#ffffff").grid(row=7, column=0, pady=5, sticky="ew")
    Button(frame, text="Cover Analizi", command=cover_analiz, font=("Arial", 12), bg="#0078d7", fg="#ffffff", activebackground="#005a9e", activeforeground="#ffffff").grid(row=8, column=0, pady=5, sticky="ew")
    Button(frame, text="Güvenlik Analizi", command=guvenlik_analiz, font=("Arial", 12), bg="#0078d7", fg="#ffffff", activebackground="#005a9e", activeforeground="#ffffff").grid(row=9, column=0, pady=5, sticky="ew")

    arayuz.mainloop()

if __name__ == "__main__":
    arayuz_baslat()