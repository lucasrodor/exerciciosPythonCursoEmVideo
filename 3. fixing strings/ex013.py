#Digite o nome de uma cidade e diga se ela começa ou não com santo
cidade = input('Digite o nome de uma cidade').strip()
print (cidade[:5].upper() == 'SANTO')
