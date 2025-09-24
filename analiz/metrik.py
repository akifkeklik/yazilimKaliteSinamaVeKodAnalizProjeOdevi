import ast
import numpy as np
from radon.metrics import mi_parameters
from radon.complexity import cc_visit
from radon.raw import analyze

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
