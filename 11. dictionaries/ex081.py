# Crie um programa que leia nome, sexo e idade de várias pessoas
# guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista, no final mostre
# A) quantas pessoas cadastradas
# B) a media de idade
# C)uma lista com mulheres
# D) uma lista com idade acima da média

dados = []

while True:
    pessoa = {}
    pessoa['nome'] = input('NOME:')
    while True:
        pessoa['sexo'] = input('SEXO [M/F]').upper()
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Dados inválidos, tente novamente!')
    pessoa['idade'] = int(input('IDADE:'))

    dados.append(pessoa)

    continuar = input('Deseja continuar? [S/N]').upper()
    if continuar == 'N':
        break
#A
print(f'A) o total de pessoas cadastradas foi {len(dados)}\n')

#B
soma = 0
for pessoa in dados:
    soma += pessoa['idade']
    media = soma / len(dados)
print(f'B) A média das idades é de {media:.2f}\n')

#C
mulheres = []
for pessoa in dados:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa["nome"])
print(f'C) Lista das mulheres: {mulheres}\n')

#D
acimaMedia = []
for pessoa in dados:
    if pessoa['idade'] > media:
        acimaMedia.append(pessoa)
print('D) Pessoas com idade acima da média:')
for pessoa in acimaMedia:
    print(f'{pessoa["nome"]} tem idade de {pessoa["idade"]} e está acima da média de {media:.2f} anos')




