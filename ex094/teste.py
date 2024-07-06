# crie um modulo chamado moedda.py que tenha as funções
# incorporadas aumentar,diminuir, dobro e metade

import moeda

p = float(input('Digite o preço:'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Auemtando 15%, temos R${moeda.aumentar(p,15)}')
print(f'Diminuindo em 20% temos R${moeda.diminuir(p,20)}')
