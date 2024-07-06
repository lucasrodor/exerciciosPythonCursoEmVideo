#Faça um programa que leia uma frase e diga quantas vezes a letra A apareceu
#Qual posição ela aparece primeiro e em qual ela aparece por ultimo

frase = input ("Digite um frase qualquer: ").strip().lower()
print (f'Frase: {frase.capitalize()}')
print (f'A letra A aparece: {frase.count("a")} vezes')
print (f'A letra A aparece pela primeira vez na posição {frase.find("a")+1}')
print (f'A letra A aparece pela ulima vez na posição {frase.rfind("a")+1}')
