ano = int(input('Qual o ano? '))
bi = ano % 4


if bi == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano é bissexto')
else:
    print('o ano nao é bissexto')