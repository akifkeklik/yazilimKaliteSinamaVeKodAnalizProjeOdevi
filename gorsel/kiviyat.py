import numpy as np
import matplotlib.pyplot as plt

def kiviyat_grafigi(veriler, kategoriler, baslik="Yazılım Kalite Analizi"):
    if len(veriler) != len(kategoriler):
        print("Hata: Veriler ve kategoriler aynı uzunlukta olmalıdır.")
        return

    veriler = np.concatenate((veriler, [veriler[0]]))
    açılar = np.linspace(0, 2 * np.pi, len(veriler))

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.fill(açılar, veriler, color='blue', alpha=0.25)
    ax.plot(açılar, veriler, color='blue', linewidth=2)

    ax.set_yticks([])
    ax.set_xticks(np.linspace(0, 2 * np.pi, len(kategoriler) + 1))
    ax.set_xticklabels(kategoriler + [kategoriler[0]])

    plt.title(baslik, size=16, weight="bold")
    plt.show()
