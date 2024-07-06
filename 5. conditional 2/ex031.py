#Calculadora de IMC

peso = float(input('Qual seu peso? (Kg)'))
h = float(input('Qual sua altura? (cm)'))
h = h/100
imc = peso / (h**2)

print (f'Seu imc é de {imc:.2f}, você está na categoria:', end= ' ')
if imc < 18.5:
    print ('ABAIXO DO PESO')
elif imc <=25:
    print ('PESO IDEAL')
elif imc <= 30:
    print ('SOBREPESO')
elif imc <=40:
    print ("OBESIDADE")
else: 
    print ('OBESIDADE MÓRBIDA')