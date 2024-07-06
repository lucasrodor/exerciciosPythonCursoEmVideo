#Um professor deseja escolher qual a ordem de apresentação
#de um grupo de alunos para apresentar um trabalho
import random
lista = []
x = int(input('Digite a quantidade de alunos que apresentarão o trabalho: '))
for i in range (x):
    y = input(f'Nome do {i+1}º aluno: ')
    lista.append(y)
ordem=lista.copy()
random.shuffle(ordem)
print (f'Os alunos que irão apresentar são: \n {lista}')
print (f'A ordem de apresentação será: \n {ordem}')


