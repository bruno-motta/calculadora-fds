class Calculadora:
    def __init__(self, numeroUm, numeroDois):
        self.numeroUm = numeroUm
        self.numeroDois = numeroDois
        

    def calculoAdicao(self):
        return self.numeroUm + self.numeroDois
    
    def calculoSubtracao(self):
        return self.numeroUm - self.numeroDois
    
    def caluloMultiplicacao(self):
        return self.numeroUm * self.numeroDois
    
    def calculoDivisao(self):
        try:
            return self.numeroUm / self.numeroDois
        except ZeroDivisionError:
            return print("DIVISÃO POR ZERO NÃO É PERMITIDA, TENTE NOVAMENTE!")    


