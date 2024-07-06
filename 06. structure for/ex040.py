#faça um programa que leia um numero e fale se ele é primo ou não

num = int(input('Digite um número inteiro: '))
divisores = 0
div = []
for i in range (1, num+1):
    if num % i == 0:
        divisores +=1
        div.append(i)
if num == 1:
    print (f'O número {num} não é primo')
if divisores <= 2:
    print (f'O número {num} é um número primo')
else:
    print (f'O número {num} não é um número primo, pois ele tem {divisores} divisores: {div}')