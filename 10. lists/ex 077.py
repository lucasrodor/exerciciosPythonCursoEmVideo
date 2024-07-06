#crie um programa que leia o nome e duas notas de varios alunos
#e guarde tudo em uma lista composta. No final mostre um boletim contendo
#a media de cada um e permita que o usuario possa mostrar as notas de cada aluno
#individualmente

boletim =[]

while True:
    nome = input('Nome do aluno')
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    media = (n1 + n2)/2
    boletim.append([nome,[n1,n2],media])

    continuar = input('Quer continuar?[S/N]').upper()
    if continuar == 'N':
        break
print(f'No.  Nome          Média')
print('-'*25)
for i, aluno in enumerate(boletim):
    print(f'{i:<4} {aluno[0]:<13} {aluno[2]:<4.2f}')

while True:
    opcao = int(input('Deseja saber as notas de qual aluno? (999 para interromper)'))
    if opcao == 999:
        print('Fim!')
        break 
    if opcao >=0 and opcao < len(boletim):
        print (f'Notas de {boletim[opcao][0]} são: {boletim[opcao][1]}')
    else:
        print('Opção inválida, tente novamente!')

