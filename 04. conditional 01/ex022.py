# faça um programa que leia três numeros e mostre qual o maior e o menor

num1 = int(input('Digite o 1º número:'))
num2 = int(input('Digite o 2º número:'))
num3 = int(input('Digite o 3º número:'))

menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num1:
    menor = num3
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print (f'O maior número é {maior} e o menor é {menor}')