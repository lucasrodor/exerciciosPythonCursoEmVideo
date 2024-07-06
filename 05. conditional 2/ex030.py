# analise a condição de existencia de um triangulo e classifique o 
# em escaleno isósceles ou equilatero

r1 = float(input("Digite o valor de uma reta: "))
r2 = float(input("Digite o valor de uma reta: "))
r3 = float(input("Digite o valor de uma reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print (f'Os segmentos {r1}, {r2}, e {r3} formam um triangulo',  end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print ('ISOSCELES')
    else: 
        print('ESCALENO')
else:
    print (f'Os segmentos {r1}, {r2}, e {r3} nao formam um triangulo')