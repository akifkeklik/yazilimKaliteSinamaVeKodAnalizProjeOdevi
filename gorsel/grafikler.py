import matplotlib.pyplot as plt
import seaborn as sns

def grafik_ciz(labels, values, title, xlabel, ylabel, palette="Blues_d"):
    plt.figure(figsize=(12, 8))
    sns.barplot(x=labels, y=values, palette=palette)
    plt.title(title, fontsize=20)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.tight_layout()
    plt.show()

def cover_orani_gorsellestir(oran: float):
    labels = ["Kaplanan Kısım", "Kaplanmayan Kısım"]
    values = [oran, 100 - oran]
    plt.figure(figsize=(8, 8))
    plt.bar(labels, values, color=["green", "gray"])
    plt.title("Kod Cover Oranı", fontsize=20)
    plt.ylabel("Oran (%)", fontsize=14)
    plt.show()

def kod_koku_gorsellestir(kokular: list):
    kokular_kategorize = {}
    for koku in kokular:
        kategori = koku.split("(")[0].strip()
        kokular_kategorize[kategori] = kokular_kategorize.get(kategori, 0) + 1

    labels = list(kokular_kategorize.keys())
    values = list(kokular_kategorize.values())

    plt.figure(figsize=(16, 10))
    sns.barplot(x=labels, y=values, palette="coolwarm")

    for i, value in enumerate(values):
        plt.text(i, value + 0.1, f"{value:.0f}", ha="center", fontsize=12)

    plt.title("Kod Koku Analizi", fontsize=24)
    plt.xlabel("Kod Koku Türleri", fontsize=18)
    plt.ylabel("Frekans", fontsize=18)
    plt.xticks(rotation=45, fontsize=14)
    plt.yticks(fontsize=14)
    plt.tight_layout()
    plt.show()
