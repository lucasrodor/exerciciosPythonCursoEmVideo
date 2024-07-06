# faça um programa que leia o nome, ,idade e sexo de 4 pessoas e 
# e mostre a media de idade, nome do homem mais velho e quantas mulheres tem menos de 20 anos

somaidade = 0
homem = 0
homemvelho =''
idadevelho = 0
mulher = 0
mulhernova = 0

for i in range (4):
    print(f'{i+1}º PESSOA')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').lower()
    somaidade += idade
    if sexo == 'm':
        homem +=1
        if idade > idadevelho:
            idadevelho = idade
            homemvelho = nome 
    elif sexo == 'f':
        mulher += 1
        if idade < 20:
            mulhernova += 1

media = somaidade/4

print (f'A média da idade das 4 pessoas é {media}')

if homem == 0:
    print ('Dentre essas pessoas, nenhuma é homem')
else:
    print (f'O nome do homem mais velho é {homemvelho} e ele tem {idadevelho} anos')

if mulher == 0:
     print('Dentre essa 4 pessoas, nenhuma é mulher')
else:        
    print (f'Dentre as mulheres, {mulhernova} tem menos que 20 anos')

