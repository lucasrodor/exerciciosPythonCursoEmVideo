# crie um pequeno sistema modularizado que permite cadastrar
# pessoas pelo seu nome e idade em um arquivo de texto simples
# O sistema só vai ter 2 opções: cadastrar ou listar as pessoas cadastradas

from lib.interface import *
pessoas_cadastradas = []
while True:
    resposta = menu(['Ver pessoas cadastradas',
                    'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        listar_pessoas(pessoas_cadastradas)
    elif resposta == 2:
        pessoa = cadastro()
        pessoas_cadastradas.append(pessoa)
    elif resposta == 3:
        print('Saindo do sistema... Até logo')
        break
    else:
        print('ERRO! Digite uma opção válida')
