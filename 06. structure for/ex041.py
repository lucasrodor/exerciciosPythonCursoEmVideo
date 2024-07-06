#faça um programa que leia uma frase ou palavra e diga se é um palindromo

frase = input('Digite uma frase ou uma palavra').strip().upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = ''
for i in range(len(juntos)-1,-1,-1):
    inverso += juntos[i]
if juntos == inverso:
    print (f'A frase {frase} é um palíndromo')
else:
    print(f'A frase {frase} não é um palíndromo')