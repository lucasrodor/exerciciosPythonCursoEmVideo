#crie um programa que leia o nome a media e a situação de um aluno, gravando em um dicionário
aluno = {}
aluno['nome'] = input('Qual o nome do aluno?')
aluno ['media'] = float(input(f'Qual a média de {aluno["nome"]} '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
else:
    aluno ['situacao'] = 'reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}').capitalize()