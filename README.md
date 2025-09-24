🧪 Yazılım Kalite ve Kod Analiz Aracı

Bu proje, Python kullanılarak geliştirilmiş bir kod kalite ve analiz aracıdır. Kod üzerinde benzerlik analizi, metrik üretimi, kod koku tespiti, güvenlik analizi ve görselleştirme yapılmasını sağlar.

🚀 Özellikler

✅ White-Box Testleri

Syntax kontrolü

Kod yapısı analizi

Kod kokusu tespiti

Magic number kontrolü

Import analizi

📊 Kod Benzerlik Analizi

Token, yapı, fonksiyon, değişken, sınıf, modül, string, yorum, döngü ve koşul yapıları karşılaştırma

🌳 Graph Analizi

AST tabanlı kod grafiği çıkarma

Graphviz ile görselleştirme

📐 Metrik Analizi

Karmaşıklık seviyeleri

Satır sayıları (kod, boş, yorum)

Fonksiyon ve değişken sayısı

Import sayısı

Yorum/Kod oranı

Ortalama karmaşıklık

👃 Kod Kokusu Tespiti

Çok uzun fonksiyonlar

Uzun parametre listeleri

Kullanılmayan fonksiyonlar

Tekrar eden kod blokları

Çok büyük sınıflar

Derin if-else zincirleri

Magic number kullanımı

🛡 Güvenlik Analizi

Tehlikeli fonksiyon (eval, exec) kullanımı

Try/Except ve with blokları

Şifre parametreleri kontrolü

📈 Görselleştirme

Bar grafikleri (benzerlik, metrikler, kokular)

Kiviyat grafiği (SonarQube benzeri kalite analizi)

Kod coverage grafiği

🖥 Kullanıcı Arayüzü (Tkinter)

Kod karşılaştırma alanları

Analiz butonları (benzerlik, graph, metrik, koku, güvenlik, coverage, kalite)

🛠 Kullanılan Teknolojiler

Python 3.x

Tkinter → GUI

unittest → White-box testler

radon → Karmaşıklık analizi

graphviz → AST görselleştirme

coverage → Kod kapsamı ölçümü

scikit-learn → Benzerlik ölçümü

matplotlib & seaborn → Grafikler

tqdm → Test ilerleme çubuğu

⚙️ Kurulum

Depoyu klonlayın:

git clone <repo-link>
cd <proje-klasörü>


Bağımlılıkları yükleyin:

pip install -r requirements.txt


⚠️ Not: tkinter Python ile birlikte gelir, requirements.txt içine yazmaya gerek yoktur.
⚠️ Ayrıca Graphviz sistem programı olarak kurulmalı ve PATH’e eklenmelidir. İndir

Programı çalıştırın:

python app.py

📌 Kullanım

Açılan arayüzde Kod-1 ve Kod-2 alanlarına Python kodlarınızı yapıştırın.

Analiz için butonları kullanın:

Benzerlik Analizi

Graph Analizi

Metrik Analizi

Kod Koku Analizi

Cover Analizi

Güvenlik Analizi

Kalite Analizi Göster

SonarQube Analizi

📊 Örnek Çıktılar

Kod benzerlik yüzdeleri

AST grafikleri (Graphviz PNG)

Kod metrik bar grafikleri

Kod kokusu dağılım grafikleri

Kod coverage oranı

SonarQube benzeri kalite analizi grafikleri

🤝 Katkıda Bulunma

Fork yapın

Yeni bir branch açın (git checkout -b feature/yenilik)

Commit atın (git commit -m "Yeni özellik eklendi")

Push edin (git push origin feature/yenilik)

Pull Request açın

📜 Lisans

📌 Bu proje eğitim amaçlıdır. Tüm hakları saklıdır.