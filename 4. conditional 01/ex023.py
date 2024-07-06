#faça um programa que mostre o salário de um funcionário 
#para salario > 1250 o aumento é de 10% se nao é de 15%

salario = float(input('Qual o seu salário?'))

if salario > 1250:
    novo = salario*1.1
else:
    novo = salario * 1.15

print (f'O salário que era de R${salario:.2f} agora é de R${novo:.2f}')