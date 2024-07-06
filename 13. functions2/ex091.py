#Faça um programa que crie uma função leiaint() que vai funcionar de forma semlhante
#a função input() do python, so que fazendo a validação para aceitar apenas um valor numerico

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            n = int(n)
            return n
            break
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
            continue



n = leiaint('Digite um número:')
print(f'Você acabou de digitar o número {n}')