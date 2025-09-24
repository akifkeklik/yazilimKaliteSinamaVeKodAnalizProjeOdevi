import ast
from graphviz import Digraph
import matplotlib.pyplot as plt

def kodu_graf_olustur(kod: str, baslik: str):
    agac = ast.parse(kod)
    graph = Digraph(comment=baslik)

    for node in ast.walk(agac):
        node_id = id(node)
        graph.node(str(node_id), type(node).__name__)
        for child in ast.iter_child_nodes(node):
            graph.edge(str(node_id), str(id(child)))

    try:
        graph.render(f"{baslik}_graph", format="png", cleanup=True)
        img = plt.imread(f"{baslik}_graph.png")
        plt.figure(figsize=(12, 8))
        plt.imshow(img)
        plt.axis('off')
        plt.title(f"{baslik} Graph Gösterimi", fontsize=20)
        plt.show()
    except FileNotFoundError:
        print("Graphviz dot executable bulunamadı. PATH ayarlarını kontrol edin.")
