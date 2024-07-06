#Faça um programa que tenha uma função chamada ficha que recebe dois parametros
#opcionais: o nome de um jogador e quants gols ele marcou. O programa deverá ser capaz
#de mostrar o jogador, mesmo que algum dado não tenha sido inserido corretamente

def ficha(jogador = '<desconhecido>',gols = 0):
    print(f'O jogador {jogador} fez {gols} gol(s) ')


nome = input('Digite o nome do jogador: ') 
gols = input('Digite a quantidade de gols: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome,gols)
    