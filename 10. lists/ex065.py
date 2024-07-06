#faça um programa que leia 5 valores numeros e coloque os numa lista, 
#no final mostre o maior, o menor e sua posição na lista

lista =[]

maior = 0
menor = maior
pos = 0
pos1 = 0
for i in range (5):
    x = int(input('Digite um número:'))
    lista.append(x)
    menor = lista[0]
for valor in lista:
    if valor > maior:
        maior = valor
        pos1 = lista.index(maior)
    if valor < menor:
        menor = valor
        pos = lista.index(menor)
print (lista)
print(f'''O maior número da lista é {maior} na posição {pos1}
e o menor é {menor} na posição {pos}''')

#outra resolução

lista = []
for i in range (5):
    x = int(input('Digite um número:'))
    lista.append(x)
maior = max(lista)
menor = min(lista)
pos = lista.index(menor)
pos1 = lista.index(maior)
print (lista)
print(f'''O maior número da lista é {maior} na posição {pos1}
e o menor é {menor} na posição {pos}''')