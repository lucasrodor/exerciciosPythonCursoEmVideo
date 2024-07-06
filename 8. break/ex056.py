# faça um programa que cadastre pessoas
# e depois mostre quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados
# e quantas mulheres tem menos de 20 anos

homens = 0
mulheres = 0
pessoas = 0
while True:
    idade = int(input('Qual a sua idade?'))
    sexo = input('Qual seu sexo? [F/M]').upper()
    continuar = input('Deseja cadastrar outra pessoas? [S/N]').upper()
    if continuar == 'N':
        break
    if idade > 18:
        pessoas += 1
    if sexo == 'M': 
        homens +=1
    if sexo == 'F' and idade < 20:
        mulheres +=1

print(f'Pessoas com mais de 18 anos: {pessoas}\nHomens cadastrados: {homens}\nMulheres com menos de 20 anos: {mulheres}')
