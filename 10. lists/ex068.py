#crie um programa que leia varios numeros inteiros, adicione em uma lista
#mostre quantos valores foram digitados, ordene em ordem decrescente e diga se o 5 esta ou nao na lista
lista = []
c = 0
while True:
    x = int(input('Digite um número:'))
    lista.append(x)
    c += 1
    resposta = input('Deseja continuar? [S/N]').upper()
    if resposta == 'N':
        break
print(lista)
print(f'A lista tem {c} números')
lista.sort(reverse=True)
print(f'Lista decrescente: \n{lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')