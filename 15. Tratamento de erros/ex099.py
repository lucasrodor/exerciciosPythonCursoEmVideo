#Faça um programa que crie uma função leiaint() que vai funcionar de forma semelhante
#a função input() do python, só que fazendo a validação para aceitar apenas um valor numérico
#fazendo o tratamento de erros

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print('ERRO! Por favor, digite um número inteiro válido')
            #volta para o início do looping
            continue
        except (KeyboardInterrupt):
            print('ERRO! O usuário interrompeu a entrada de dados')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print('ERRO! Por favor, digite um número real válido')
            #volta para o início do looping
            continue
        except (KeyboardInterrupt):
            print('ERRO! O usuário interrompeu a entrada de dados')
            return 0
        else:
            return n


numint = leiaint('Digite um número inteiro:')
numreal = leiafloat('Digite um número real:')
print(f'Numero inteiro: {numint}\nNumero real: {numreal}')