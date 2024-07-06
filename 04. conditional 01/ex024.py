#faça um programa que analise a condiçao de existencia de um triangulo

r1 = float(input("Digite o valor de uma reta: "))
r2 = float(input("Digite o valor de uma reta: "))
r3 = float(input("Digite o valor de uma reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print (f'Os segmentos {r1}, {r2}, e {r3} formam um triangulo')
else:
    print (f'Os segmentos {r1}, {r2}, e {r3} nao formam um triangulo')
