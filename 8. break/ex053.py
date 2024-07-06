#programa que leia números inteiros e pare quando for digitado o num 999, mostre a soma e quantos foram digitados
soma = 0
quant = 0
while True:
    n = int(input('Digite um número'))
    if n == 999:
        break
    soma +=n
    quant += 1

print(f'Foram digitados {quant} números e a soma deles é de {soma}')