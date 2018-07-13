class Fracao:

    def __init__(self, numerador, denominador):
        if (denominador >= 0):
            self.numerador = numerador
            self.denominador = denominador
        else:
            print("Denominador inválido")

    def valor_real(self):
        return str(self.numerador) + "/" + str(self.denominador)

    def soma(self, f2):
        df = self.mmc(self.denominador, f2.denominador)
        n1 = (df / self.denominador) * self.numerador
        n2 = (df / f2.denominador) * f2.numerador
        return str(int(n1) + int(n2)) + "/" + str(df)

    def dif(self, f2):
        df = self.mmc(self.denominador, f2.denominador)
        n1 = (df / self.denominador) * self.numerador
        n2 = (df / f2.denominador) * f2.numerador
        return str(int(n1) - int(n2)) + "/" + str(df)

    def mult(self, f2):
        r = Fracao(1,1)
        r.numerador = self.numerador * f2.numerador
        r.denominador = self.denominador * f2.denominador
        return str(r.numerador) + "/" + str(r.denominador)

    def div(self, f2):
        r = Fracao(1,1)
        r.numerador = self.numerador * f2.denominador
        r.denominador = self.denominador * f2.numerador
        return str(r.numerador) + "/" + str(r.denominador)

    def denominador_zero(self, f2):
            return True if self.denominador != 0 & f2.denominador != 0 else False

    def mmc(self,n1, n2):
        if (n1> n2):
            maior = n1
        else:
            maior = n2
        for i in range(maior+1):
            aux = n1 * i
            if (aux % n2) == 0:
                _mmc = aux
        return _mmc


if __name__ == '__main__':
    f1 = Fracao(1,2)
    f2 = Fracao(2,4)
    res = f1.soma(f2)
    res2 = f1.dif(f2)
    res3 = f1.mult(f2)
    res4 = f1.div(f2)
    print(res)
    print(res2)
    print(res3)
    print(res4)