# crie um modulo chamado moedda.py que tenha as funções
# incorporadas aumentar,diminuir, dobro e metade

import moeda

p = float(input('Digite o preço:'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Auemtando 15%, temos {moeda.aumentar(p,15,True)}')
print(f'Diminuindo em 20% temos {moeda.diminuir(p,20,True)}')
