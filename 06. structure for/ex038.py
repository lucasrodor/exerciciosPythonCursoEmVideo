#faça um programa que leia seis numeros inteiros e calcule a soma dos pares
soma = 0
for i in range (6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma = soma + num
print (f'A soma dos números é {soma}')