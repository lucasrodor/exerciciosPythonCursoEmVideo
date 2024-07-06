def metade(n=0, formato=False):
    res = n/2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n*2
    return res if formato is False else moeda(res)


def aumentar(n=0, aumento=0, formato=False):
    res = n + ((aumento/100)*n)
    return res if formato is False else moeda(res)


def diminuir(n, diminuir=0, formato=False):
    res = n * (100-diminuir)/100
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
