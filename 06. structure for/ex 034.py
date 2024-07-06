#crie um programa que faça uma contagem regressiva de 10 segundos
from time import sleep

for i in range (10,-1,-1):
    print(i)
    sleep(1)