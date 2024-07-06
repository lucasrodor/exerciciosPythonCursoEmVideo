#crie uma lista que tenha o nome e peso de varias pessoas e mostre os mais leves e mais pesados

pessoas = []
pessoa = []
maior = menor = 0
while True:
    pessoa.append(input('Nome:'))
    pessoa.append(float(input('Peso:')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1]>maior:
            maior = pessoa[1]
        if pessoa[1]< menor:
            menor = pessoa[1]

    pessoas.append(pessoa[:])
    pessoa.clear()
    continuar= input('Deseja continuar? [S/N]').upper()
    if continuar == 'N':
        break

print(f'Pessoas cadastradas: {len(pessoas)}')
print(f'O menor peso foi de {menor}Kg. Peso de: ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]',end = ' ')
print('')
print(f'O maior peso foi de {maior}Kg. Peso de:',end='')
for p in pessoas:
    if p[1]== maior:
        print(f'[{p[0]}]',end=' ')