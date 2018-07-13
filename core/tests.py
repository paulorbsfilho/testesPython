import unittest
from .fracao import *


class TestFracao(unittest.TestCase):

    def test_fracao(self):
        f = Fracao(1,2)
        res = f.valor_real()
        self.assertEqual(res,"1/2")

    def test_operacao_soma_com_fracao(self):
        f1 = Fracao(1,2)
        f2 = Fracao(2,4)
        res = f1.soma(f2)
        self.assertEqual(res, "8/8")

    def test_operacao_dif_com_fracao(self):
        f1 = Fracao(1,2)
        f2 = Fracao(2,4)
        res = f1.dif(f2)
        self.assertEqual(res, "0/8")

    def test_operacao_mult_com_fracao(self):
        f1 = Fracao(1,2)
        f2 = Fracao(2,4)
        res = f1.mult(f2)
        self.assertEqual(res, "2/8")

    def test_operacao_div_com_fracao(self):
        f1 = Fracao(1,2)
        f2 = Fracao(2,4)
        res = f1.div(f2)
        self.assertEqual(res, "4/4")

if __name__ == '__main__':
    unittest.main()