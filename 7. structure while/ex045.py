#faça um programa que leia o sexo do usuario e so aceite M ou F, caso contrario peça para o usuario digitar novamente

sexo = input('Qual o seu sexo? M/F').upper()
while sexo not in 'MF':
        print('Digite o seu sexo novamente')
        sexo = input('Qual o seu sexo? M/F').upper()
if sexo == 'M':
        print ('Você é do sexo masculino')
if sexo == 'F':
        print('Você é do século feminino')
