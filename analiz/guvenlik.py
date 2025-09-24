import ast

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
    return issues
