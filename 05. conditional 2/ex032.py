# # elabore um programa que calcule o valor a ser pago por um produto
# considerando o seu preço normal e condição de pagamento
# à vista dinheiro/ cheque - 10%off, cartao 5%off, 2x cartao nada e 3x ou mais 20% juros

preco = float(input('Qual o preço do produto?'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão de débito
[ 3 ] Em 2x no cartão de crédito
[ 4 ] Em 3x ou mais no cartão de crédito''')
pag = int(input('Qual a opção?'))
if pag == 1:
    desc = preco*0.1
    preco1 = preco - desc
    print (f'''A compra de R${preco} vai sair por R${preco1:.2f}
Você obteve 10% de desconto e economizou R${desc:.2f}''')
elif pag == 2:
    desc = preco*0.05
    preco1 = preco - desc
    print (f'''A compra de R${preco} vai sair por R${preco1:.2f}
Você obteve 10% de desconto e economizou R${desc:.2f}''')
elif pag == 3:
    parcelas = 2
    total = preco/parcelas
    print (f'''O valor da compra será de R${preco:.2f}
divido em 2 parcelas de R${total:.2f}''')

elif pag == 4:
    parcelas = int(input('Quantas parcelas?'))
    juros = preco*0.2
    total = preco + juros
    print (f'''Sua compra será parcelada em {parcelas}X de R${total/parcelas:.2f} com juros
O valor final será de R${total:.2f}''')

else: 
    print ('Escolha uma opção de pagamento válida')