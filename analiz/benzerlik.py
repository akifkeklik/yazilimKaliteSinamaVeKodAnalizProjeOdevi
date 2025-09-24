import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def kod_benzerlik_hesapla(kod1: str, kod2: str) -> dict:
    if not kod1 or not kod2:
        raise ValueError("Kodlar boş olamaz.")

    # 1. Token Benzerliği
    vectorizer = CountVectorizer().fit_transform([kod1, kod2])
    token_benzerlik = cosine_similarity(vectorizer)[0][1]

    # Yardımcı Fonksiyonlar
    def agac_vektor(agac):
        return [type(node).__name__ for node in ast.walk(ast.parse(agac))]

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
    degisken_benzerlik = len(
        set(metinleri_ayristir(kod1, ast.Name)).intersection(metinleri_ayristir(kod2, ast.Name))
    ) / max(len(set(metinleri_ayristir(kod1, ast.Name)) | set(metinleri_ayristir(kod2, ast.Name))), 1)

    # 4. Fonksiyon Adları Benzerliği
    fonksiyon_benzerlik = len(
        set(metinleri_ayristir(kod1, ast.FunctionDef)).intersection(metinleri_ayristir(kod2, ast.FunctionDef))
    ) / max(len(set(metinleri_ayristir(kod1, ast.FunctionDef)) | set(metinleri_ayristir(kod2, ast.FunctionDef))), 1)

    # 5. Sınıf Adları Benzerliği
    sinif_benzerlik = len(
        set(metinleri_ayristir(kod1, ast.ClassDef)).intersection(metinleri_ayristir(kod2, ast.ClassDef))
    ) / max(len(set(metinleri_ayristir(kod1, ast.ClassDef)) | set(metinleri_ayristir(kod2, ast.ClassDef))), 1)

    return {
        "Token Benzerliği": token_benzerlik * 100,
        "Yapısal Benzerlik": yapisal_benzerlik * 100,
        "Değişken Adları Benzerliği": degisken_benzerlik * 100,
        "Fonksiyon Adları Benzerliği": fonksiyon_benzerlik * 100,
        "Sınıf Adları Benzerliği": sinif_benzerlik * 100,
    }
