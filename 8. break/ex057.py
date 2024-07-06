#crie um programa que leia o nome e o preço de um produto, no final mostre o total,
#quantos custam mais de 1000 e o mais barato

total = 0
mais = 0
menorpreco = 0
menorproduto = ''
cont = 0
while True:
    prod = input('Produto: ')
    preco = float(input('Preço: '))
    cont +=1
    total += preco
    if preco > 1000:
        mais += 1
    if cont == 1 or preco < menorpreco:
        menorpreco = preco
        menorproduto = prod
    continua = input('Deseja continuar? [S/N]').upper()
    if continua == 'N':
        break
 

print (f'''O total da compra foi de R${total:.2f}
Temos {mais} produtos que custaram mais de R$1000,00
e o mais barato foi {menorproduto} que custou R${menorpreco:.2f}''')    