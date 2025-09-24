import ast

def kod_kokularini_tespit_et(kod: str) -> list:
    kokular = []
    for node in ast.walk(ast.parse(kod)):
        if isinstance(node, ast.FunctionDef) and len(node.body) > 30:
            kokular.append(f"Fonksiyon {node.name} çok uzun ({len(node.body)} satır)")
        if isinstance(node, ast.FunctionDef) and len(node.args.args) > 5:
            kokular.append(f"Fonksiyon {node.name} çok fazla parametre alıyor ({len(node.args.args)} parametre)")
        if isinstance(node, ast.ClassDef) and len(node.body) > 100:
            kokular.append(f"Çok büyük sınıf: {node.name} ({len(node.body)} satır)")
    return kokular
