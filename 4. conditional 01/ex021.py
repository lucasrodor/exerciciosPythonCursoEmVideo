#faça um programa que le o ano e fala se ele é bissexto ou não
from datetime import date
ano = int(input('Qual ano deseja analisar se é bissexto? Digite 0 para o ano atual'))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano %100 != 0 or ano % 400 == 0:
    print (f'O ano de {ano} é um ano bissexto')
else:
    print (f'O ano de {ano} não é um ano bissexto')
