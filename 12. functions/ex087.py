from random import randint

def sorteia (numeros):
    for i in range (5):
        x = randint(0,100)
        numeros.append(x)
    print (f'Os números sorteados foram {numeros}')


def soma_par(numeros):
    pares =[]
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
    for j in pares:
        soma += j
    print (f'Dentre os numeros da lista, os numeros {pares} são pares e a soma é {soma}')


numeros =[]
sorteia(numeros)
soma_par(numeros)
