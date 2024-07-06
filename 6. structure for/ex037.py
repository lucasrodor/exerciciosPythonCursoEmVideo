#faça um programa que mostre a tabuada de um número

x = int(input('Deseja saber a tabuada de qual número?'))
print (f'Tabuada do {x}')
for i in range (1,11):
    tabuada = x*i
    print (f'{x} X {i} = {tabuada}')
    