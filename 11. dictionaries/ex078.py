#crie um programa onde 4 jogadores joguem um dado e armazene o resultado em um dicionario
#ordene em ordem e mostre o vencedor (maior número)
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1,6),
        'jogador 2': randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)}
ranking={}
#cria uma lista com tupla ordenadas
ranking =sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Valore sorteados:')
print('-'*30)
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep (0.7)
print('-'*30)
print('resultado')
for i, v in enumerate(ranking):
    print(f'{i+1}ºLugar: {v[0]} com {v[1]}')
    sleep(0.7)
