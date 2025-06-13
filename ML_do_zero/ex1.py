tempo = float(input('Qual o tempo gasto da viagem? '))
velocidade = int(input('Qual a velociade media durante a viagem? '))

distancia = tempo * velocidade
litros = distancia / 12

print(f'a quantidade de litros é de {litros}')