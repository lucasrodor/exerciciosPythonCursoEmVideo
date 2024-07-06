from random import randint

print('Pensei em número de 0 a 10, você consegue adivinhar?')
adv = randint(0,10)
user = int(input('Qual número eu pensei?'))
while adv != user:
    if user < adv:
        print('Mais...')
        user = int(input('Tente novamente'))
    else:
        print('Menos...')
        user = int(input('Tente novamente'))
if user == adv:
    print (f'Parabéns, você acertou! Eu pensei no número {adv}')