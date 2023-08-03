#Faça uma função calculadora que os números e as operações serão feitas pelo usuário.
#O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair.
#No início, o programa mostrará a seguinte lista de operações:

def calcular(operacao, num1, num2):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2
    else:
        return None

print("==== Calculadora ====")
print("Operações disponíveis:")
print("1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair")

while True:
    opt = int(input("\nDigite a operação desejada: "))

    if opt == 0:
        break
    elif opt not in (1, 2, 3, 4):
        print("Opção inválida. Digite um número válido.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = calcular(opt, num1, num2)

    if resultado is not None:
        print("Resultado é:", resultado)

print("Calculadora encerrada.")







