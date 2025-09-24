import coverage
import os

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
