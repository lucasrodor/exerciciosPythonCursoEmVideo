#Faça um programa que tenha uma função contador que receba ter parametros
# inicio, fim, passo, seu programa tem que realizar as tres contagens através da função
# a) 1-10 de 1 em 1
# b)10 - 0 de 2 em 2
# c) personalizada
from time import sleep
def contador(inicio,fim,passo):
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range (1,11,1):
        print(i, end =' ')
        sleep(0.3)
    print('FIM')
    print('-'*30)
    print('Contagem de 10 até 0 de 2 em 2')
    for j in range (10,-1,-2):
        print(j, end=' ')
        sleep (0.3)
    print('FIM')
    print('-' *30)

    print('Contagem personalizada')
    if passo == 0:
        passo =1
    if inicio > fim:
        passo = -abs(passo)
    else:
        passo = abs(passo)
    for l in range (inicio,fim + (1 if passo > 0 else -1),passo):
        print (l, end = ' ')
        sleep (0.3)
    print('FIM')



inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))

contador(inicio,fim,passo)