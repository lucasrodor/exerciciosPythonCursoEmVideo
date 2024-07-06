#Classico da média
n1 = float (input('Digite a primeira nota'))
n2 = float (input('Digite a segunda nota'))
n3 = float (input('Digite a terceira nota'))
media = (n1 + n2 +n3)/3

if media >= 7:
    print (f'Você teve nota {media:.1f} | APROVADO')
elif media >= 5 and media < 7:
    print (f'Você teve nota {media:.1f} | RECUPERAÇÃO')
else:
    print (f'Você teve nota {media:.1f} | REPROVADO')