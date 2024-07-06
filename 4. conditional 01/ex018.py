#escreva um programa que leia a velocidade do carro e fale se ele vai ser multado ou nao
#além disso, mostre o valor da multa (R$7,00/Km/h)

vel = float(input("Qual a velocidade do carro?"))
multa = 7*(vel-80)
if vel > 80:
    print ('MULTADO')
    print (f'Você ultrapassou a velocidade permitida em {vel -80}Km/h')
    print (f'A multa é de R${multa:.2f}')
else:
    print ('Velocidade permitida!')