#faça um programa que leia o primeiro termo e a razão e mostre os 10 primeiros termos de uma P.A

a1  = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))

for i in range (10):
    termo = a1
    a1 += razao
    print (f'{termo} ', end='-> ')
print ('Fim')