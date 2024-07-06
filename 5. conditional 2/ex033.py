from random import randint
from time import sleep
itens= ('pedra', 'papel', 'tesoura')
computador = randint (0,2)

print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''' )

jogada = int(input('Qual a sua jogada?'))
print ('JO')
sleep(0.5)
print ('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print (f'COMPUTADOR {itens[computador]} X {itens[jogada]} JOGADOR')

if jogada == computador:
    print('EMPATE')
if jogada == 0: #jogador jogou pedra
    if computador == 1:#computador jogo papel
        print(f'O computador GANHOU')
    elif computador == 2:#computador jogou tesoura
        print('O jogador GANHOU')
elif jogada == 1:#jogador jogou papel
    if computador == 0:#computador jogou pedra
        print ('O jogador GANHOU')
    elif computador == 2:#computador jogou tesoura
        print ('O computador GANHOU')

elif jogada == 2: #jogador jogou tesoura:
    if computador == 0:#O Computador jogou peda
        print('O computador GANHOU')
    elif computador == 1:#O computador jogou papel
        print('O jogador GANHOU')
else:
    print('Jogada inválida')