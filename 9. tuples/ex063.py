#crie uma tupla que tenha um produto e seu preço e mostre isso de forma tabular

produtos = 'pão', 1.50, 'leite', 4.00, 'queijo', 8.00, 'presunto', 8.00, 'suco', 6.00, 'chocolate', 10.5,'vinho', 150
print('-'*38)
print(f'{"TABELA DE PREÇO": ^38}')
print('-'*38)
for i in range (len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f'R${produtos[i]: >6.2f}', end ='\n')