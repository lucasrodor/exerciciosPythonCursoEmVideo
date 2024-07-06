#crie um programa que leia varios numeros e adicione em uma lista, depois pegue os pares em uma lista
#e os impares em outra e no final mostre as três

lista = []
pares = []
impares = []

while True:
    x = int(input('Digite um número:'))
    lista.append(x)
    resposta = input('Deseja continuar? [S/N]').upper()
    if resposta == 'N':
        break
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(lista)
print(pares)
print(impares)

