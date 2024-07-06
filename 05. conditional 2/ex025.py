casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o valor do salário?'))
finan = int(input('De quantos anos vai ser o financiamento'))
parcela = casa / (finan*12)
if parcela >= 30/100*salario:
    print(f'O salário é de R${salario} e parcela é de R${parcela}, portanto')
    print('Emprestimo negado')
else:
    print(f'O salário é de R${salario:.2f} e parcela é de R${parcela:.2f}')
    print('Portanto, emprestimo aceito')