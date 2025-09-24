from analiz.benzerlik import kod_benzerlik_hesapla
from analiz.metrik import metrik_uret
from analiz.kod_koku import kod_kokularini_tespit_et
from analiz.cover import cover_orani_hesapla
from analiz.guvenlik import kod_guvenligi_ve_hata_tahmini
from analiz.graph import kodu_graf_olustur

from gorsel.grafikler import grafik_ciz, kod_koku_gorsellestir, cover_orani_gorsellestir
from gorsel.kiviyat import kiviyat_grafigi

from utils.sartname import sartname_ekrani
import tkinter as tk
from tkinter import messagebox


# Yazılım Kalite Analizi (özet pencere)
def yazilim_kalite_analizi(kod: str):
    kalite_penceresi = tk.Toplevel()
    kalite_penceresi.title("Yazılım Kalite Analizi")
    kalite_penceresi.geometry("600x400")
    kalite_penceresi.configure(bg="#f0f4f7")

    metrikler = metrik_uret(kod)
    kokular = kod_kokularini_tespit_et(kod)

    kalite_verileri = f"""
    - Karmaşıklık Seviyesi: {metrikler['Karmaşıklık Seviyesi']}
    - Toplam Satır: {metrikler['Toplam Satır']}
    - Boş Satır: {metrikler['Boş Satır']}
    - Yorum Satırı: {metrikler['Yorum Satırı']}
    - Fonksiyon Sayısı: {metrikler['Fonksiyon Sayısı']}
    - Değişken Sayısı: {metrikler['Değişken Sayısı']}
    - Kod Koku Sayısı: {len(kokular)}
    """

    tk.Label(kalite_penceresi, text="Yazılım Kalite Analizi",
             font=("Arial", 16, "bold"), bg="#f0f4f7").pack(pady=10)
    tk.Label(kalite_penceresi, text=kalite_verileri,
             font=("Arial", 12), bg="#f0f4f7", justify="left").pack(anchor="w", padx=20, pady=10)

    kalite_penceresi.mainloop()


# SonarQube tarzı kalite analizi göster
def kalite_analiz_goster(kod: str):
    metrikler = metrik_uret(kod)
    kategoriler = ["Karmaşıklık", "Toplam Satır", "Boş Satır", "Yorum Satırı", "Fonksiyon Sayısı"]
    veriler = [
        metrikler['Karmaşıklık Seviyesi'],
        metrikler['Toplam Satır'],
        metrikler['Boş Satır'],
        metrikler['Yorum Satırı'],
        metrikler['Fonksiyon Sayısı']
    ]
    kiviyat_grafigi(veriler, kategoriler, "SonarQube Kalite Analizi")


# Kullanıcı Arayüzü
def arayuz_baslat():
    arayuz = tk.Tk()
    arayuz.title("Kod Analiz Aracı")
    arayuz.geometry("800x600")
    arayuz.configure(bg="#f0f4f7")

    frame = tk.Frame(arayuz, bg="#f0f4f7")
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Kod giriş alanları
    tk.Label(frame, text="Kod-1'inizi aşağıya yapıştırınız:",
             font=("Arial", 14), bg="#f0f4f7").grid(row=0, column=0, sticky="w")
    metin_alani1 = tk.Text(frame, wrap='word', height=10,
                           font=("Arial", 12), bg="#ffffff", fg="#000000")
    metin_alani1.grid(row=1, column=0, sticky="nsew")

    tk.Label(frame, text="Kod-2'nizi aşağıya yapıştırınız:",
             font=("Arial", 14), bg="#f0f4f7").grid(row=2, column=0, sticky="w")
    metin_alani2 = tk.Text(frame, wrap='word', height=10,
                           font=("Arial", 12), bg="#ffffff", fg="#000000")
    metin_alani2.grid(row=3, column=0, sticky="nsew")

    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(3, weight=1)

    # Buton fonksiyonları
    def benzerlik_analiz():
        kod1 = metin_alani1.get("1.0", tk.END).strip()
        kod2 = metin_alani2.get("1.0", tk.END).strip()
        if kod1 and kod2:
            benzerlik = kod_benzerlik_hesapla(kod1, kod2)
            grafik_ciz(list(benzerlik.keys()), list(benzerlik.values()),
                       "Kod Benzerlik Analizi", "Kriterler", "Benzerlik (%)")

    def graph_analiz():
        kod1 = metin_alani1.get("1.0", tk.END).strip()
        if kod1:
            kodu_graf_olustur(kod1, "Kod-1")

    def metrik_analiz():
        kod1 = metin_alani1.get("1.0", tk.END).strip()
        if kod1:
            metrikler1 = metrik_uret(kod1)
            grafik_ciz(list(metrikler1.keys()), list(metrikler1.values()),
                       "Kod Metrikleri", "Metrikler", "Değerler")

    def kod_koku_analiz():
        kod1 = metin_alani1.get("1.0", tk.END).strip()
        if kod1:
            kokular1 = kod_kokularini_tespit_et(kod1)
            kod_koku_gorsellestir(kokular1)

    def cover_analiz():
        kod1 = metin_alani1.get("1.0", tk.END).strip()
        kod2 = metin_alani2.get("1.0", tk.END).strip()
        if kod1 and kod2:
            cover_orani = cover_orani_hesapla(kod1, kod2)["Cover Oranı"]
            cover_orani_gorsellestir(cover_orani)

    def guvenlik_analiz():
        kod1 = metin_alani1.get("1.0", tk.END).strip()
        kod2 = metin_alani2.get("1.0", tk.END).strip()
        results = {}
        if kod1:
            results["Kod-1"] = kod_guvenligi_ve_hata_tahmini(kod1)
        if kod2:
            results["Kod-2"] = kod_guvenligi_ve_hata_tahmini(kod2)
        if results:
            output = "".join([f"{key}: " + "\n".join(val) + "\n\n" for key, val in results.items()])
            print(output)

    # Butonlar
    tk.Button(frame, text="Benzerlik Analizi", command=benzerlik_analiz,
              font=("Arial", 12), bg="#0078d7", fg="#ffffff").grid(row=4, column=0, pady=5, sticky="ew")
    tk.Button(frame, text="Graph Analizi", command=graph_analiz,
              font=("Arial", 12), bg="#0078d7", fg="#ffffff").grid(row=5, column=0, pady=5, sticky="ew")
    tk.Button(frame, text="Metrik Analizi", command=metrik_analiz,
              font=("Arial", 12), bg="#0078d7", fg="#ffffff").grid(row=6, column=0, pady=5, sticky="ew")
    tk.Button(frame, text="Kod Koku Analizi", command=kod_koku_analiz,
              font=("Arial", 12), bg="#0078d7", fg="#ffffff").grid(row=7, column=0, pady=5, sticky="ew")
    tk.Button(frame, text="Cover Analizi", command=cover_analiz,
              font=("Arial", 12), bg="#0078d7", fg="#ffffff").grid(row=8, column=0, pady=5, sticky="ew")
    tk.Button(frame, text="Güvenlik Analizi", command=guvenlik_analiz,
              font=("Arial", 12), bg="#0078d7", fg="#ffffff").grid(row=9, column=0, pady=5, sticky="ew")
    tk.Button(frame, text="Kalite Analizi Göster", command=lambda: yazilim_kalite_analizi(metin_alani1.get("1.0", tk.END).strip()),
              font=("Arial", 12), bg="#0078d7", fg="white").grid(row=10, column=0, pady=5, sticky="ew")
    tk.Button(frame, text="SonarQube Analizi", command=lambda: kalite_analiz_goster(metin_alani1.get("1.0", tk.END).strip()),
              font=("Arial", 12), bg="#0078d7", fg="white").grid(row=11, column=0, pady=5, sticky="ew")

    arayuz.mainloop()


# Program giriş noktası
if __name__ == "__main__":
    sartname_ekrani()
    arayuz_baslat()
