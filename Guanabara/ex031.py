d = int(input('Qual a distancia da sua viagem? '))

# if d <= 200:
#     calc1 = d * 0.5
# else:
#     calc1 = d * 0.45

# print('o custo da sua viagem sera de R${:.2f}'.format(calc1))

calc1 = d * 0.5 if d <= 200 else d * 0.45

print('o custo da sua viagem sera de R${:.2f}'.format(calc1))