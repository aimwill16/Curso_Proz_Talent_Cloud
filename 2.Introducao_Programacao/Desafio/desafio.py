# Faça um programa que tenha uma lista de produtos, adicione, remova e mostre os itens.

produtos = ["Abacate","Maça","Banana","Uva"]

def mostra_produto(produto):
    for item in produto:
        print(item, end=' ')
def adiciona_item(produtos):
    adc = produtos.append(input("Digite o produto para acrescentar: \n"))

def remove_produto(produtos):
    rm = input("Digite o produto para remover: \n")
    try:
        for i in produtos:
            if i == rm:
                produtos.remove(rm)
                print(f"Produto '{rm}' removido.")
    except:
        print("Produto não encontrado")

print("===   Gerenciador de Estoque - Frutas   ====")
verificador = False
try:
    while verificador == False:
        opt = int(input("\n\nDigite o numero da opção: \n"
                        "1. Mostrar itens em estoque.\n"
                        "2. Adicionar itens em estoque.\n"
                        "3. Remover itens em estoque.\n"
                        "4. Sair do programa\n"))

        if opt == 1:
            mostra_produto(produtos)
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