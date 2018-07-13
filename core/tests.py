import unittest
from .fracao import *


class TestFracao(unittest.TestCase):

    def test_fracao(self):
        f = Fracao(1,2)
        exp = f.valor_real()
        self.assertEqual(exp,"1/2")

    def test_operacao_soma_com_fracao(self):
        f1 = Fracao(1,2)
        f2 = Fracao(2,4)
        exp = f1.soma(f2)
        self.assertEqual(exp, "8/8")

    def test_operacao_dif_com_fracao(self):
        f1 = Fracao(1,2)
        f2 = Fracao(2,4)
        exp = f1.dif(f2)
        self.assertEqual(exp, "0/8")

    def test_operacao_mult_com_fracao(self):
        f1 = Fracao(1,2)
        f2 = Fracao(2,4)
        exp = f1.mult(f2)
        self.assertEqual(exp, "2/8")

    def test_operacao_div_com_fracao(self):
        f1 = Fracao(1,2)
        f2 = Fracao(2,4)
        exp = f1.div(f2)
        self.assertEqual(exp, "4/4")
        
    def test_div_por_zero(self):
        f1 = Fracao(1,2)
        f2 = Fracao(2,0)
        exp = f1.div(f2)


if __name__ == '__main__':
    unittest.main()