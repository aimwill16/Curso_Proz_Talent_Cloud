# Faça um programa que tenha uma lista de produtos, adicione, remova e mostre os itens.

produtos = ["Abacate","Maça","Banana","Uva"]

def mostra_produto(itens):
    for i in itens:
        print(i, end=" ")
def adiciona_item(produtos):
    adc = produtos.append(input("Digite o produto para acrescentar: \n"))

def remove_produto(produtos):
    rm = input("Digite o produto para remover: \n")
    for i in produtos:
        if i == rm:
            produtos.remove(rm)
            print(f"Produto '{rm}' removido.")
    if i != rm:
        print(f"Produto '{rm}' não encontrado")

print("===   Gerenciador de Estoque - Frutas   ====")
verificador = False
try:
    while verificador == False:
        opt = int(input("\nOpções:\n"
                        "1. Mostrar itens em estoque.\n"
                        "2. Adicionar itens em estoque.\n"
                        "3. Remover itens em estoque.\n"
                        "4. Sair do programa\n"
                        "\nDigite a opção desejada:\n"))

        if opt == 1:
            print("Os itens atuais são:")
            mostra_produto(produtos)
            print("")
        elif opt == 2:
            adiciona_item(produtos)
        elif opt == 3:
            remove_produto(produtos)
        elif opt == 4:
            verificador = True
        else:
            print("Opção errada, por favor, digite novamente.")


except:
    print("Opção errada, por favor digite um número.")