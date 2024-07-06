#crie um programa que tenha uma função chamada voto que vai receber como parametro
#o ano de nascimento de uma pessoa, retornando um valor literal caso o jogo seja obrigatorio
# nao permitido ou opcional

def voto(ano_nasc):
    idade = 2023 - ano_nasc
    if idade <= 16:
        print (f'Com a idade de {idade} anos o seu voto é NEGADO')
    elif idade > 65 or 16 <= idade <18:
        print (f'Com a idade de {idade} anos o seu voto é OPICIONAL')
    else:
        print (f'Com a idade de {idade} anos o seu voto é OBRIGATÓRIO')


voto(2010)