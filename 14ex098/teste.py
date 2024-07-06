# crie uma função chamada leiadinheiro() que funciona como
# o input mas com uma validação de dados

from utilidadesCEV import moeda, dado

p = dado.leiadinheiro("Digite o preço: R$")
moeda.resumo(p, 10, 10)
