#Desenvolva um programa que recebe do usuário nome completo e
# ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e
# a idade que completou, ou completará, no ano atual (2022).
#Caso o usuário não digite um número ou apareça um inválido no campo do ano,
#o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

dadosCorretos = False
while(dadosCorretos == False):
    try:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite o ano de nascimento: "))
        if 1922 < idade < 2021:
            dadosCorretos = True
            idadeAtual = 2022 - idade
            print("Seu nome é: ", nome, " e sua idade atual é: ", idadeAtual, "anos.")
        else:
            print("Por favor, insira um ano entre 1922 e 2021.")

    except:
        print("Dados incorretos")
