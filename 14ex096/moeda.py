def metade(n=0, formato=False):
    res = n/2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n*2
    return res if formato is False else moeda(res)


def aumentar(n=0, taxa=0, formato=False):
    res = n + ((taxa/100)*n)
    return res if formato is False else moeda(res)


def diminuir(n, taxa=0, formato=False):
    res = n * (100-taxa)/100
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(n=0, taxaaumento=0, taxareducao=0, formato=False):
    print('-'*36)
    print(f'{"RESUMO DO VALOR":^36}')
    print('-'*36)
    print(f'preço analisado: \t{moeda(n)}')
    print(f'dobro do preço: \t{dobro(n,True)}')
    print(f'metade do preço: \t{metade(n,True)}')
    print(f'aumentando {taxaaumento}%: \t{aumentar(n,taxaaumento,True)}')
    print(f'reduzindo {taxareducao}%: \t\t{diminuir (n,taxareducao,True)}')
    print('-'*36)
