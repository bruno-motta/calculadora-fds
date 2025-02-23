class Calculadora:
    def __init__(self, numeroUm, numeroDois):
        self.numeroUm = numeroUm
        self.numeroDois = numeroDois
        self.historicOperacao = [] #lista vazia, armazena as informações

    def calculoAdicao(self):
        result = self.numeroUm + self.numeroDois
        self.historicOperacao.append(f"{self.numeroUm} + {self.numeroDois} = {result}") #regitra e grava na ultima posição da lista .append()
        return result

    def calculoSubtracao(self):
        result = self.numeroUm - self.numeroDois
        self.historicOperacao.append(f"{self.numeroUm} - {self.numeroDois} = {result}")
        return result

    def calculoMultiplicacao(self):

        result = self.numeroUm * self.numeroDois
        self.historicOperacao.append(f"{self.numeroUm} * {self.numeroDois} = {result}")
        return result
        

    def calculoDivisao(self):
        try:
            result = self.numeroUm / self.numeroDois
            self.historicOperacao.append(f"{self.numeroUm} / {self.numeroDois} = {result}")
            return result
        except ZeroDivisionError:
            print("DIVISÃO POR ZERO NÃO É PERMITIDA, TENTE NOVAMENTE!")
            return None
        
    def Historico(self):
        if not self.historicOperacao:
            print("Nenhuma operação realizada ainda.")
        else:
            print("Histórico de operações:")
            for operacao in self.historicOperacao:
                print(operacao)

    def limpHistorico(self):
        self.historico.clear()
        print("Histórico de operações apagado com sucesso!")

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

