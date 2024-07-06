#crie um programa que leia 7 numeros e se for par ou impar adicione-os em suas respectivas listas
numeros = [[],[]]
for i in range (7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print(numeros)
numeros[0].sort()
print(f'Numeros pares: {numeros[0]}')
numeros[1].sort()
print(f'Numeros ímpares: {numeros[1]}')
