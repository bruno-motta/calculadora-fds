from Calculadora import Calculadora

escolherOperacao = input("Digite (1) para Adição, (2) para Subtração, (3) para Multiplicação ou (4) para Divisão: ")

calcConta = Calculadora(int(input("Digite o primeiro numero para o calculo: ")), int(input("Digite o segundo numero para o calculo: ")))

if escolherOperacao == 1:
    print("Resultado: ", calcConta.calculoAdicao())

elif escolherOperacao == 2:
    print("Resultado: ", calcConta.calculoSubtracao())
    
elif escolherOperacao == 3:
    print("Resultado: ", calcConta.caluloMultiplicacao())

elif escolherOperacao == 4:
    print("Resultado: ", calcConta.calculoDivisao())
else:
    print("ESCOLHA INCORRETA, TENTE NOVAMENTE!")