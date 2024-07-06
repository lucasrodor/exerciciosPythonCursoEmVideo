#faça um programa que faça um jogo de par ou ímpar e interrompa quando o jogador
#perder, e mostre quantas vezes ele ganhou

import random
vitorias = 0
while True:
    computador = random.randint(1,10)
    jogador = int(input('Jogue um número: '))
    jogada = input('Par ou Ímpar [P/I]').upper()
    soma = computador + jogador
    if jogada == 'P':
        print (f'Você escolheu par e jogou {jogador}\nO computador jogou {computador}')
        if soma %2 == 0:
            print (f'A soma {soma} deu par, você venceu!')
            vitorias += 1
        else:
            print(f'A soma {soma} deu ímpar, você perdeu!')
            break
    elif jogada == 'I':
        print (f'Você escolheu ímpar e jogou {jogador}, e o computador {computador}')
        if soma %2 == 0:
            print (f'A soma {soma} é ímpar, você perdeu!')
            break
        else:
            print(f'A soma {soma} é par, você venceu!')
            vitorias +=1
print (f'Números de vitórias consecutivas: {vitorias}')
