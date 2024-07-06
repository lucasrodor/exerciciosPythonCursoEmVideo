#melhore o exercicio anterior pedindo se o usuario quer mostrar mais
# números e mostre no final quantos foram digitador

a1 = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razao da PA'))
n = 0
total = 0
mais = 10
while mais != 0: 
    total += mais
    while n <total:
        termo = a1
        a1+= razao
        n += 1
        print (f'{termo}', end = ' -> ')
    print('Pausa')
    mais = int(input('Deseja mostrar mais quantos termos?'))
print('FIM')
print(f'Nessa PA foram mostrados {n} termos')