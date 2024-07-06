# faça um programa que mostre a tabuada do numero que o usuario digitar e pare quando o numero digitado for negativo

i = 1
while True:
    n = int(input('Deseja saber a tabuada de qual número?'))
    if n < 0:
        print('Programa encerrado!')
        break
    i=1
    print (f'TABUADA DO {n}')
    while i <11:
        result = n * i
        print (f'{n} X {i} = {result}')
        i+=1
    