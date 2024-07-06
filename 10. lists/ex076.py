from random import randint
from time import sleep
#faça um programa que crie "palpites" para um jogo da mega sena

palpites=[]
x = int(input('Quantos jogos deseja sortear?'))
for i in range (x):
    jogos = []
    while len(jogos)<6:
        num = randint(1,60)
        if num not in jogos:
            jogos.append(num)
    jogos.sort()
    palpites.append(jogos)
c = 1
print('Palpites da Mega Sena:')
for a in palpites:
    print(f'Jogo {c}: {a}')
    c +=1
    sleep(0.5)
