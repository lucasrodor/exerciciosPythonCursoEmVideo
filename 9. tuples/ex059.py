#escreva uma tupla com os times do brasileirao e mostre os 5 primeiros colocados
#os 4 ultimos, a posição que o flamengo está e uma lista em ordem alfabetica

times = ("Athletico-PR", "Bahia", "Flamengo", "Botafogo", "Cruzeiro",
        "Atlético-MG", "Bragantino", "Palmeiras", "São Paulo",
          "Internacional", "Fortaleza", "Grêmio", "Vasco", "Criciúma",
            "Juventude", "Corinthians", "Fluminense", "Vitória", "Atlético-GO", "Cuiabá")
print (f'Os 5 primeiros colocados do Brasileirão são:\n{times[:5]}')
print(f'Os últimos 4 colocados do Brasileirão são:\n{times[16:]}')
print(f'O flamengo está na {times.index("Flamengo")+1}º posição')
print (sorted(times))