#17 pitagoras
# catop = float(input('Digite o valor do cateto oposto: '))
# catadj = float(input('Digite o valor do cateto adjacente: '))
# hipo = (catop**2 + catadj**2)**(1/2)
# print (f'O valor da hipotenusa é: {hipo}')

import math
catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
hipot= math.hypot (catop, catadj)
print (f' o valor da hipotenusa é {hipot:.2f}')