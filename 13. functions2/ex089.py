# Faça um programa que tenha uma função fatorial() que receba dois parametros
# o primeiro que indique o número a calcular e o outro chamado show, que sera um valor
# logico(opcional) indicando se será mostrado ou não na teala o processo de calculo do fatorial

def fatorial(numero, show=False):
    """Calcula o Fatorial de um número

    Args:
        numero (int): número que será calculado
        show (bool, optional):  Mostrar ou não a conta

    Returns: O valor do fatorial
    """
 
    fatorial = 1
    if numero == 1 or numero == 0:
        return 1
    else:
        for i in range(numero, 0, -1):
            if show:
                if i > 1:
                    print(f'{i} x',end =' ')
                else:
                    print(f'{i} =', end = ' ')
            fatorial *= i
        return fatorial

help(fatorial)
print(f'Fatorial é {fatorial(52)}')
