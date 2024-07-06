#crie um codigo que preenche uma matriz e o usuario escolha o seu formato


l= int(input('Número de linhas:'))
c = int(input('Número de colunas:'))
matriz = []
for i in range (l):
    linha = []
    for j in range (c):
        x = int(input(f'Digite o valor para a posição [{i+1},{j+1}]:'))
        linha.append(x)
    matriz.append(linha)
for linha in matriz:
    print(linha)