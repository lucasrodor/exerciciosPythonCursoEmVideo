#faça um programa que mostre a sequencia de fibonacci escolhendo quantos termos vao ser mostrados
tamanho = int(input('Quantos termos deseja mostrar?'))
n=2
termos= 1
termoant = 0
termoatual = 1

print (f'{termoant}-{termoatual}', end = '-')

while n < tamanho:

    novotermo = termoant + termoatual 
    termoant= termoatual
    termoatual = novotermo
    n += 1
    print (novotermo, end ='-')
    
print ('FIM')

   