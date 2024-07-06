# Crie um programa que vai ler o nome do jogador e quantas partidas.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicioinario incluindo o total de gols
# feitos durante o campeonato

from time import sleep

dados = {}
nGols = []

dados ['nome']= input('Qual o nome do jogador?')
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou?'))

if partidas > 0:
    for i in range (partidas):
        gols = int(input(f'Quantos gols na partida {i+1}?'))
        nGols.append(gols)

else:
    print(f'O jogador {dados["nome"]} não jogou nenhuma partida!')

dados['gols'] = nGols
dados['total'] = sum(nGols)

for k,v in dados.items():
    print(f'O campo {k} tem valor {v}')

print('-='*15)

for i, gols in enumerate (nGols):
    print(f'Na partida {i+1}, {dados["nome"]} marcou {gols} gol(s)')
    sleep(0.5)
    
print(f'No total, {dados["nome"]} marcou {dados["total"]} gols')