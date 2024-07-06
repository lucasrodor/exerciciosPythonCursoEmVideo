#Digite o nome completo e mostre ele em letras maiusculas, letras minusculas
#a quantidade de letras sem espaço e a quantidade de letras do primeiro nome

nome = input('Digite seu nome completo').strip()
print (f'Seu nome completo é {nome}')
print (f'O nome em maiúsculas é {nome.upper()}')
print (f'O nome em minusculas é {nome.lower()}')
print (f'O seu nome possui {len(nome) - nome.count(" ")} letras')
separa = nome.split()
print (f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')