#16 digite um numero real qualquer e mostre a sua porção inteira
from math import trunc
x = float(input('Digite um numero real qualquer:'))
print (f'A parte real do numero {x} é {trunc(x)}')