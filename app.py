from Calculadora import Calculadora  

numeroUm = int(input("Digite o primeiro número para o cálculo: "))
numeroDois = int(input("Digite o segundo número para o cálculo: "))

calcConta = Calculadora(numeroUm, numeroDois)

escolherOperacao = int(input("Digite (1) para Adição, (2) para Subtração, (3) para Multiplicação ou (4) para Divisão: "))

calcConta.calcular(escolherOperacao)