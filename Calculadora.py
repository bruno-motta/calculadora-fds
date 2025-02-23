class Calculadora:
    def __init__(self, numeroUm, numeroDois):
        self.numeroUm = numeroUm
        self.numeroDois = numeroDois

    def calculoAdicao(self):
        return self.numeroUm + self.numeroDois

    def calculoSubtracao(self):
        return self.numeroUm - self.numeroDois

    def calculoMultiplicacao(self):
        return self.numeroUm * self.numeroDois

    def calculoDivisao(self):
        try:
            return self.numeroUm / self.numeroDois
        except ZeroDivisionError:
            print("DIVISÃO POR ZERO NÃO É PERMITIDA, TENTE NOVAMENTE!")
            return None

    def calcular(self, operacao):
        
        if operacao == 1:
            print("Resultado:", self.calculoAdicao())

        elif operacao == 2:
            print("Resultado:", self.calculoSubtracao())

        elif operacao == 3:
            print("Resultado:", self.calculoMultiplicacao())

        elif operacao == 4:
            resultado = self.calculoDivisao()
            if resultado is not None:  
                print("Resultado:", resultado)

        else:
            print("ESCOLHA INCORRETA, TENTE NOVAMENTE!")