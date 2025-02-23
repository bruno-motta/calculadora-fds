from Calculadora import Calculadora  

while True:
    escolherOperacao = int(input("\nDigite (1) para Adição, (2) para Subtração, (3) para Multiplicação, (4) para Divisão ou (0) para sair: "))

    if escolherOperacao == 0:
        print("\nSaindo da calculadora...")
        break  

    numeroUm = int(input("Digite o primeiro número para o cálculo: "))
    numeroDois = int(input("Digite o segundo número para o cálculo: "))

    calcConta = Calculadora(numeroUm, numeroDois)
    calcConta.calcular(escolherOperacao)

    
    print("\nHistórico de operações:")
    calcConta.Historico()