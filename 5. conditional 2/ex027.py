#faça um programa que leia a data de nascimento e informe de acordo com a idade
#se ele ainda vai se alistar, se é a hora de alistar ou se ja passou da hora
#mostre o tempo que falta ou que passou do prazo
from datetime import date
ano = int(input('Qual o seu ano de nascimento?'))
alist = ano + 18
atual = date.today().year
idade = atual - ano

if idade < 18:
    saldo = 18 - idade
    print (f'Quem nasceu em {ano} tem {idade} anos')
    print (f'Você ainda não precisa se alistar, só daqui {saldo} ano(s), em {alist}')
elif idade > 18:
    saldo = idade - 18
    print (f'Quem nasceu em {ano} tem {idade} anos')
    print (f'Seu prazo para alistamento já passou')
    print (f'Você deveria ter se alistado em {alist}, {saldo} ano(s) atrás')
else:
    print (f'Você tem {idade} anos, e no ano de {atual}\nvocê deve se alistar IMEDIATAMENTE')
