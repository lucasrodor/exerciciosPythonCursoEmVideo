def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


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


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc

def cadastro():
    idade = leiaint('Qual a sua idade: ')
    try:
        nome = str(input('Qual o seu nome: '))
    except (TypeError,ValueError):
        print('Digite um nome válido')
    
    return {'Nome': nome, 'Idade': idade}

def listar_pessoas(pessoas):
    if not pessoas:
        print ('Nenhuma pessoa cadastrada')
    else:
        c = 1
        for pessoa in pessoas:
            print(f'{c} - Nome: {pessoa["Nome"]} | Idade:{pessoa["Idade"]}')
            c+=1
