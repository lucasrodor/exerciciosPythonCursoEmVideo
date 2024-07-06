#crie um programa que gere uma tupla com 5 numero aleatorios
#depois mostre ela e mostre o maior e o menor valor
import random

numeros = ()
while len(numeros)<5:
    valor = random.randint(1,100)
    numeros += (valor,)
print (numeros)
# maximo = max(numeros)
# minimo = min(numeros)
# print(f'O maior valor é {maximo} e o menor é {minimo}')
maior = numeros[1]
menor = numeros[1] 
for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i]<menor:
        menor = numeros[i]
print(f'O maior valor é {maior} e o menor é {menor}')