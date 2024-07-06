#crie um programa que leia dois numeros e de ao usuario a escolha de qual operação deseja fazer

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''[1] soma
[2] subtração
[3] multiplicação
[4] divisão
[5] sair do programa\n''' )
    opcao = int(input('Qual opção deseja realizar?'))
    if opcao == 1:
        print (f'A soma entre {num1} e {num2} é {num1+num2}\n')
    if opcao == 2:
        print (f'A diferença entre {num1} e {num2} é {num1-num2}\n')
    if opcao == 3:
        print(f'A multiplicação entre {num1} e {num2} é {num1*num2}\n')
    if opcao == 4:
        print (f'A divisão de {num1} por {num2} é {num1/num2}\n')
print ('Programa encerrado!')