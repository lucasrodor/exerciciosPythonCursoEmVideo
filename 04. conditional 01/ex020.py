#calcule o preço da viagem. 0,50 por KM para viagens de até 200 km e 0,45 para mais longas

dist = float(input('Qual a distância da viagem?'))
preco = 0
if dist <= 200:
    preco = dist * 0.5
    print (f'A viagem de {dist}km custará R${preco}')
else:
    preco = dist * 0.45
    print (f'A viagem de {dist} km custará R${preco:.2f}')
    