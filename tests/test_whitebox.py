import unittest
import ast
from tqdm import tqdm

class WhiteBoxTest(unittest.TestCase):
    def test_kod_syntaxi(self):
        kod = "def ornek_fonksiyon():\n    print('Merhaba')"
        try:
            ast.parse(kod)
        except SyntaxError as e:
            self.fail(f"Syntax hatası: {e}")

    def test_kod_yapisi(self):
        kod = "def ornek_fonksiyon(a, b):\n    return a + b"
        tree = ast.parse(kod)
        fonksiyonlar = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        self.assertIn("ornek_fonksiyon", fonksiyonlar)

if __name__ == "__main__":
    print("White-Box Testleri Başlatılıyor...")
    test_suite = unittest.TestLoader().loadTestsFromTestCase(WhiteBoxTest)
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
