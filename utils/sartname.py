from tkinter import Tk, Label, Button, messagebox

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

    def reddet():
        sartname_penceresi.destroy()
        messagebox.showinfo("Şartname Reddedildi", "Şartname reddedildi. Program sonlanıyor.")
        exit()

    Button(sartname_penceresi, text="Kabul Ediyorum", command=kabul_et,
           font=("Arial", 12), bg="#0078d7", fg="white").pack(side="left", padx=20, pady=20)

    Button(sartname_penceresi, text="Reddet", command=reddet,
           font=("Arial", 12), bg="#d9534f", fg="white").pack(side="right", padx=20, pady=20)

    sartname_penceresi.mainloop()
