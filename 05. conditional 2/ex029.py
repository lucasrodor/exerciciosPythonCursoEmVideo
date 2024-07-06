#faça um programa que classifique a categoria do atleta de acordo com a idade dele
from datetime import date
ano = int(input('Digite seu ano de nascimento'))
atual = date.today().year
idade = atual - ano

print (f'O atleta tem {idade} anos')
if idade <= 9:
    print ('Categoria MIRIM')
elif idade <= 14:
    print ('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print ('Categoria SÊNIOR')
else:
    print ('Categoria MASTER')