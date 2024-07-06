#crie um programa que permita o usuario digitar varios valores em uma lista
#caso ele ja exista na lista nao sera adicionado, depois mostre em ordem crescente

lista = []
quant = int(input('Digite quantos números deseja adicionar:'))
for i in range (quant):
    x = int(input('Digite um número para a lista:'))
    if x not in lista:
        lista.append(x)
print(lista)
print(f'lista em ordem crescente:\n{sorted(lista)}')