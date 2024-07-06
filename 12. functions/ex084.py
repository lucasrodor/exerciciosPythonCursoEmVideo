# Faça um pograma que tenha uma função chamada escreva que receba um texto como parametro
# e imprima ele na seguinte forma:
# -------
#  texto
# -------
# de forma adaptavel

def escreva(msg):
    largura = len(msg)+4
    print('-'*largura)
    print(f'{msg:^{largura}}')
    print('-'*largura)

mensagem = input('Escreva uma mensagem:')
escreva(mensagem)