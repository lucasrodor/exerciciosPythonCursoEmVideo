#faça um program que calcule a soma dos numeros impares multiplos de 3 de 1 a 500

for i in range (1,501,2):
    if i % 3 == 0:
        soma = soma + i
print(soma)