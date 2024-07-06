# jogo de adivinhação, faça um programa em que o pc "pense" em um número e voce adivinhe
from random import randint

numpc = randint(0,5)
print ('Pensei em um número de 0 a 5, quero ver você adivinhar!\nQual número eu pensei?\n')
resposta = int(input())
if resposta == numpc:
    print (f'Parabens, você acertou! Eu pensei no número {numpc}')
else:
    print (f'Você errou! Eu pensei no número {numpc}')
