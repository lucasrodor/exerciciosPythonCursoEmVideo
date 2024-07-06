#crie um programa que leia numeros inteiros, e no final mostre a média
#quantos foram digitados e o maior e o menor valor

resp = ''
num = 0
quant = 0
media = 0
soma = 0
while resp != 'n':
    num = int(input('Digite um número'))
    soma +=num
    quant +=1
    media = soma/quant
    if quant == 1:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    resp = input('Deseja continuar? [S/N]').lower()
print (f' O maior valor é {maior}, o menor é {menor}, a média é de {media} e foram digitados {quant} números')