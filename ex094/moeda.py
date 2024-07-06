def metade(n):
    return n/2


def dobro(n):
    return n*2


def aumentar(n, aumento):
    n = n + ((aumento/100)*n)
    return n


def diminuir(n, diminuir):
    n = n * (100-diminuir)/100
    return n
