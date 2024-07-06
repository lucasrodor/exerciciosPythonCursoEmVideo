#faça um conversor de bases numericos de decimal para binario, octal e hexagonal

num = int(input('Digite um número:'))
print('''Escolha uma das opções abaixo
      [ 1 ] binario
      [ 2 ] octal
      [ 3 ] hexadecimal''')
opcao = int(input('Sua opção:'))
    
if opcao == 1:
    print (f'O número {num}, em binário é {bin(num)[2:]}')
elif opcao == 2:
    print (f'O numero {num} em octal é {oct(num)[2:]}')
elif opcao == 3:
    print (f'O numero {num} em Hexadecimal é {hex(num)[2:]}')
else: 
    print ('Digite uma opção válida')