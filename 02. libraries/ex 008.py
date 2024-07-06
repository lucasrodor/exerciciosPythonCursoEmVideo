#18 seno cosseno e tangente
import math
angulo=float(input('Digite o valor do angulo em º: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print (f'O valor de seno de {angulo}º é {sen:.3f}')
print (f'O valor de cosseno de {angulo}º é {cos:.3f}')
print (f'O valor de tangente de {angulo}º é {tan:.3f}')

#*biblioteca math tem a função sin cos e tan, mas precisa estar em radianos
#para transformar para radianos é preciso usar maht.radians()