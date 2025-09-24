# 🧪 Yazılım Kalite ve Kod Analiz Aracı

Bu proje, Python kullanılarak geliştirilmiş **kod kalite ve analiz aracı**dır. Kod üzerinde **benzerlik analizi, metrik üretimi, kod koku tespiti, güvenlik analizi ve görselleştirme** yapılmasını sağlar.

---

## 🚀 Özellikler

- ✅ **White-Box Testleri**
  - Kodun syntax kontrolü
  - Kod yapısı analizi
  - Kod kokuları testi
  - Magic number tespiti
  - Import kontrolü

- 📊 **Kod Benzerlik Analizi**
  - Token benzerliği
  - Yapısal benzerlik
  - Değişken adları benzerliği
  - Fonksiyon adları benzerliği
  - Sınıf adları benzerliği
  - Modül benzerliği
  - String benzerliği
  - Yorum satırları benzerliği
  - Döngü türleri benzerliği
  - Koşul yapıları benzerliği

- 🌳 **Graph Analizi**
  - AST tabanlı kod grafiği çıkarır
  - Graphviz ile görselleştirme

- 📐 **Metrik Analizi**
  - Karmaşıklık seviyeleri
  - Satır sayıları (kod, boşluk, yorum)
  - Fonksiyon ve değişken sayısı
  - Import sayısı
  - Yorum/Kod oranı
  - Ortalama karmaşıklık

- 👃 **Kod Kokusu Tespiti**
  - Çok uzun fonksiyonlar
  - Uzun parametre listeleri
  - Kullanılmayan fonksiyonlar
  - Tekrar eden kod blokları
  - Çok büyük sınıflar
  - Derin if-else zincirleri
  - Magic number kullanımları

- 🛡 **Güvenlik Analizi**
  - Tehlikeli fonksiyon (eval, exec) kullanımı
  - Try/Except blokları
  - With blokları
  - Şifre parametreleri

- 📈 **Görselleştirme**
  - Bar grafikleri (kod benzerliği, metrikler, kod kokuları)
  - Kiviyat grafiği (SonarQube benzeri kalite analizi)
  - Kod coverage oranı grafiği

- 🖥 **Kullanıcı Arayüzü (Tkinter)**
  - Kod karşılaştırma alanları
  - Benzerlik analizi butonu
  - Graph analizi butonu
  - Metrik analizi butonu
  - Kod kokusu analizi butonu
  - Cover analizi butonu
  - Güvenlik analizi butonu
  - Kalite analizi ekranı

---

## 🛠 Kullanılan Teknolojiler

- **Python 3.x**
- **Tkinter** → Kullanıcı arayüzü  
- **unittest** → White-box testler  
- **radon** → Metrik hesaplama, karmaşıklık analizi  
- **graphviz** → AST görselleştirme  
- **coverage** → Kod kapsamı ölçümü  
- **sklearn** → Kod benzerlik ölçümü  
- **matplotlib & seaborn** → Grafikler  
- **tqdm** → Test ilerleme çubuğu  

---

## ⚙️ Kurulum

1. Depoyu klonlayın:
```bash
git clone <repo-link>
cd <proje-klasörü>
```

2. Gerekli bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

> requirements.txt içeriği:
```txt
tk
graphviz
radon
coverage
scikit-learn
matplotlib
seaborn
tqdm
```

3. Programı çalıştırın:
```bash
python proje.py
```

---

## 📌 Kullanım

- Program açıldığında **kod yapıştırma alanlarına** Kod-1 ve Kod-2 yazabilirsiniz.  
- Analiz için butonları kullanın:  
  - `Benzerlik Analizi` → Kod karşılaştırma  
  - `Graph Analizi` → AST grafiği üretme  
  - `Metrik Analizi` → Satır, karmaşıklık vb. metrikler  
  - `Kod Koku Analizi` → Kod kokusu tespiti  
  - `Cover Analizi` → Coverage hesaplama  
  - `Güvenlik Analizi` → Güvenlik açıkları tarama  
  - `Kalite Analizi Göster` → Kalite ekranı  
  - `SonarQube Analizi` → Kiviyat grafiği  

---

## 📊 Örnek Çıktılar

- Kod benzerlik yüzdeleri  
- AST grafiği (Graphviz PNG)  
- Kod metrik bar grafikleri  
- Kod kokusu dağılım grafikleri  
- Kod coverage oranı  

---

## 🤝 Katkıda Bulunma

1. Fork yapın  
2. Yeni bir branch açın (`git checkout -b feature/yenilik`)  
3. Commit atın (`git commit -m "Yeni özellik eklendi"`)  
4. Push edin (`git push origin feature/yenilik`)  
5. Pull Request açın  

---

## 📜 Lisans

Bu proje eğitim amaçlıdır. Tüm hakları saklıdır.
