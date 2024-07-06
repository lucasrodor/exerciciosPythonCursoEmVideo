# crie um programa que leia nome, ano de nascimento
# e carteira de trabalho e cadastre-os (com idade) em um dicionario,
# se por acaso o CTPS for diferente de zero, o dicionario recebrá
# também o ano de contratação e salário. Calcule e acrescente, alem da idade
# com qunatos anos a pessoa vai se aposentar

from datetime import datetime

dados = {}
dados['nome'] = input('Nome:')
nasc = int(input('Ano de nascimento'))
ano = datetime.now().year
dados['idade'] = ano - nasc
dados ['CTPS'] = int(input('CTPS (0 se não tem):'))
if dados ['CTPS'] == 0:
    for k, v in dados.items():
        print(f'O {k} tem valor {v}')
else:
    dados['ano de contratação'] = int(input('Ano de contratação:'))
    dados['salário'] = float(input('Salário:'))
    dados['aposentadoria'] = dados['ano de contratação'] +35
    dados ['idade de aposentadoria'] = dados['aposentadoria'] - nasc
    for k, v in dados.items():
        print(f'O {k} tem valor {v}')
