# crie uma tupla com várias palavras e depois mostre as vogais que tem em cada uma delas
palavras = ('legal', 'ciencia', 'programaçao', 'testar',
            'estudo', 'inteligencia', 'artifical', 'final')
vogais =('a','e','i','o','u')
for i in palavras:
    print(f'\nNa palavras {i} temos:',end =' ')
    for j in i:
        if j in vogais:
            print(j, end=' ')
