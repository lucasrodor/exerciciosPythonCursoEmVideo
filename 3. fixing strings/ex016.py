#Digite um nome e mostre o primeiro e o ultimo nome da pessoa que digitou

nome = input('Digite seu nome completo:\n').strip()
nome1= nome.split()
print ('Muito prazer em te conhecer!')
print (f'Seu primeiro nome é {nome1[0]}')
print (f'Seu último nome é {nome1[-1]}')