#leia o primeiro termo e a razao de uma pa e mostre os 10 primeiros termos

a1 = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razao da PA'))
n = 1
while n <11:
    termo = a1
    a1 += razao
    n += 1
    print (f'{termo}', end = ' -> ')
print ('Fim')
