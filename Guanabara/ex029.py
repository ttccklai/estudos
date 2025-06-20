veloc = int(input('Qual sua velocidade atual? '))
multa = (veloc - 80) * 7
if veloc >= 80:
    print('você está acima da velocidade e será multado em R${:.2f}'.format(multa))
else:
    print('você está dentro da velocidade permitida')