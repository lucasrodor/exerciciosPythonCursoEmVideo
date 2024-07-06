#faça um programa que tenha uma função chamada área que leia a largura e comprimento e mostre a área
def area(l,c):
    area = l*c
    print(f'A área do terreno que de {l}x{c} é de {area}m2')

print('-'*30)
print('Área do terreno:')
print('-'*30)

largura = float(input('Qual o tamanho da largura?'))
comprimento = float(input('Qual o tamanho do comprimento?'))
area(largura,comprimento)