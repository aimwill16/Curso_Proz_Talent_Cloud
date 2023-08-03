#Faca uma funcao calculadora de dois numeros com tres paramentos: numeros da operacao(2) e a operacao
#1 p/ soma, 2 p/ subtracao, 3 p/ multiplicacao e 4 p/ divisao

print("==== Calculadora ===")

num1 = float(input("\nDigite o primeiro número da operação: "))
num2 = float(input("Digite o segundo número da operação: "))

print("\n(1 = Soma, 2 = Subtração, 3 = Multiplicação e 4 = Divisão)")
operador = int(input("Digite o operador: "))

def calculadora(num1, num2, operador):
    resultado = 0
    if operador == 1:
        return num1 + num2

    elif operador == 2:
        return num1 - num2

    elif operador == 3:
        return num1 * num2

    elif operador == 4:
        return num1 / num2

    else:
        print("Operador inválido")
        print(resultado)

resultado = calculadora(num1, num2, operador)
if resultado is not None:
    print("Resultado: ", resultado)