#calcule o fatorial de um número usando o loop while
num = int(input('Deseja saber o fatorial de qual número?'))
fat = 1
aux = num
while aux > 1:
    fat *= aux
    aux -= 1
print (f'O fatorial de {num} é {fat}')