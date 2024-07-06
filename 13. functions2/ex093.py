#Faça um mini-sistema que utilize o interactive help do Python
#O usuário vai digitar o comando e o manual vai aparecer. Quando o
#usuário digitar a palavra "FIM", o programa se encerrará.
def ajuda (com):
    help(com)


def titulo (msg, cor=0):
    tam = len (msg) + 4
    print('~' *tam)
    print(f'  {msg}')
    print('~' * tam)

comando = ''
while True:
    titulo ('SISTEMA DE AJUDA PYHELP')
    comando = input('Função ou biblioteca >')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
print('ATÉ LOGO')
