#faça um programa que leia o peso de 5 pessoas e diga o maior e o menor

maior = 0
menor = 0
for i in range (5):
    peso = float(input(f'Qual o peso da {i+1}º pessoas?'))
    if i == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso 
    
print(f'O maior peso foi {maior}Kg e o menor peso foi {menor}Kg')