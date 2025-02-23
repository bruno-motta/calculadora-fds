from Calculadora import Calculadora

escolherOperacao = int(input("Digite (1) para Adição, (2) para Subtração, (3) para Multiplicação ou (4) para Divisão: "))

numeroUm = int(input("Digite o primeiro número para o cálculo: "))
numeroDois = int(input("Digite o segundo número para o cálculo: "))

calcConta = Calculadora(numeroUm,numeroDois )

if escolherOperacao == 1:
    print("Resultado: ", calcConta.calculoAdicao())

elif escolherOperacao == 2:
    print("Resultado: ", calcConta.calculoSubtracao())

elif escolherOperacao == 3:
    print("Resultado: ", calcConta.calculoMultiplicacao())

elif escolherOperacao == 4:
    resultado = calcConta.calculoDivisao()
    if resultado is not None:  
        print("Resultado: ", resultado)

else:
    print("OPÇÃO INCORRETA, ESCOLA UM NUMERO DE 1 À 4!")