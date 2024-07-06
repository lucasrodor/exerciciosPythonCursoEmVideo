#mostre a soma de todos os valores digitados em uma matriz
#a soma da terceira coluna
#o maior valor da segunda linha

matriz=[]
somaPar = 0
par =0
soma3 =0
maior = 0
for l in range (3):
    linha=[]
    for c in range(3):
        x = int(input(f'Digite o número da posição [{l+1}{c+1}]'))
        linha.append(x)
        if len(linha) == 3:
            soma3 += linha[2]
    matriz.append(linha)
for i in range (3):
    for j in range (3):
        if matriz[i][j] %2 == 0:
            par = matriz[i][j]
            somaPar+=par
maior = max(matriz[1])
print(f'Matriz 3x3:')
for linha in matriz:
    print(linha)
    
print(f'A soma dos números pares é {somaPar}')
print(f'A soma dos elementos da 3º coluna é {soma3}')
print(f'O maior valor da 2º coluna é {maior}')

