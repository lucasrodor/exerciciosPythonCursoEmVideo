#faça um codigo que o usuario preencha uma matriz 3x3

matriz = []
for i in range (3):
    linha = []
    for j in range (3):
        x = int(input(f'Digite o valor para a posição [{i+1},{j+1}]:'))
        linha.append(x)
    matriz.append(linha)

for linha in matriz:
    print(linha)
