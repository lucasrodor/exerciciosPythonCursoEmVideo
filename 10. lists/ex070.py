#crie um programa que leia uma expressão matemática e mostre se os parenteses estão na ordem certa

x = input('Digite uma expressão matemática: (com parênteses)')
abertos = 0
correto = True
for i in x:
    if i == '(':
        abertos += 1
    elif i == ')':
        if abertos == 0:
            correto = False
            break
        abertos -=1

if abertos != 0:
    correto = False
print(x)
if correto:
    print('A expressão contém os parênteses escritos da forma correta')
else:
    print('Os parênteses estão errados!')