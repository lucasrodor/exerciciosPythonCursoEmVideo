def leiadinheiro(msg):
    valido = False
    while not valido:
        #recebe o numero como string para trata-lo, troca , por . e verifica se é alfa numérico
        entrada = input(msg).replace(',','.').strip()
        # validar se é alfanumerico
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! "{entrada}" é um preço inválido')
        else:
            #quebra o looping
            valido = True
            #transforma a entrada que era uma string em um número float e retorna ele para a variável
            return float(entrada)
