#Usuario entra com os seguintes dados

quantidade_rodas = int(input("Digite a quantidade de rodas do veiculo:"))
peso_bruto = float(input("Digite o peso bruto do veiculo:"))
pessoas = int(input("Quantas pessoas estão no veiculo?"))

if (quantidade_rodas == 2) or (quantidade_rodas == 3):
    print("Categoria A")
elif (quantidade_rodas == 4) and (pessoas <= 8) and (peso_bruto <= 3500):
    print("Categoria B")
elif (quantidade_rodas >= 4) and (peso_bruto > 3500) and (peso_bruto <= 6000):
    print("Categoria C")
elif (quantidade_rodas >= 4) and (pessoas > 8):
    print("Categoria D")
elif (quantidade_rodas >= 4) or (peso_bruto > 6000):
    print("Categoria E")
