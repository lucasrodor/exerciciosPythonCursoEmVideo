#faça um programa que leia a idade de 7 pessoas e diga quais são maiores de idade
from datetime import date
maioridade = 0
menoridade = 0
ano = date.today().year
for i in range (7):
    nasc = int(input(f'Em que ano a {i+1}º pessoa nasceu?\n'))
    idade = ano - nasc
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print (f'Dentre essas pessoas, {maioridade} são maiores de idade e {menoridade} são menores')
