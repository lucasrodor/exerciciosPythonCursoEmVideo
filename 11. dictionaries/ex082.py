#Crie um programa que aprimore o exercicio 80 para que ele funcione com 
#varios jogadores, incluindo um sistema de visualização de detalhes do 
#aproveitamento de cada jogador

from time import sleep

jogador = {}
gols = []
time = []
while True:
    jogador.clear()
    jogador ['nome']= input('Qual o nome do jogador?')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))

    gols.clear()
    if partidas > 0:
        for i in range (partidas):
            gols.append(int(input(f'Quantos gols na partida {i+1}?')))
            
    else:
        print(f'O jogador {jogador["nome"]} não jogou nenhuma partida!')

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())


    continuar = input('Deseja continuar? [S/N]').upper()
    if continuar == 'N':
        break
print('-='*30)
print('cod',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ',end ='')
    for d in v.values():
        print(f'{str(d):<15}', end ='')
    print()
print('-'*40)
while True:
    opcao = int(input('Qual jogador deseja analisar os dados? (999 interrompe)'))
    if opcao == 999:
        break
    if opcao >= len(time):
        print(f'ERRO, não existe jogador com código {opcao}')
    else:
        print(f'-------- Levantamento do jogador {time[opcao]["nome"]} ')
        for i, g in enumerate (gols):
            print(f'    No jogo {i+1} fez {g} gols.')
print('-'*40)
print('Programa encerrado!')

