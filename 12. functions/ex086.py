# Faça um programa que tenha uma função chamada maior(), que receba 
# vários inteiros. Seu programa tem que analisar todos os valores e 
# dizer qual deles é o maior

def maior (*num):
    print('Analisando os valores passados...')
    maior = num[0]
    for i in num:
        print(i,end = ' ')
        if i > maior:
            maior = i
    print (f'Ao todo foram analisados {len(num)} números e o maior valor é {maior}')
        

maior(1,2,3,6,8,4)
maior (3,6,2,9)
maior(0)
maior (109,39,349,293,425,19)
