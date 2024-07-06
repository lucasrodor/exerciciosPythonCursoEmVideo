#crie um programa que leia 4 numeros e mostre quantas vezes apareceu o valor 9, 
#em qual posição apareceu o valor 3 e quais numeros são pares

numeros = ()
while len(numeros) < 4:
    num = int(input('Digite um número'))
    numeros +=(num,)
print(f'O valor 9 apareceu {numeros.count(9)}X')
if 3 in numeros:
    print(f'O numero 3 aparece na posição {numeros.index(3)+1}')
else: 
    print('O valor 3 não foi digitado em nenhuma posição')
print('Números pares: ')
for i in range (len(numeros)):
    if numeros[i] % 2 == 0:
        print(f'O número {numeros[i]} é par')