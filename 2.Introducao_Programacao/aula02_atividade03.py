#Precisamos imprimir um número para cada andar de um hotel de 20 andares.
#O dono é supersticioso e optou por não ter o 13ro andar.
#Como desafio, imprima eles em ordem decrescente.

for i in range(20):
    if i != 13:
        print(i)

print("============ Outra forma ============")

j = 0
while j < 20:
    if j != 13:
        print(j)
    j = j + 1

print("============ Outra forma ============")

numeros = [i for i in range(20) if i != 13]
print(numeros)

print("============ Forma decrescente ============")

for i in range(20, 0, -1):
    if i != 13:
        print(i)
