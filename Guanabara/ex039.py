from datetime import date as dt

ano = int(input('Digite o ano que você nasceu: '))

ano_atual = dt.today().year

idade = ano_atual - ano

if idade < 18:
    print('Você tem só {} anos e ainda faltam {} anos para se alistar.'.format(idade, 18 - idade))
    print('Você deverá se alistar em {}.'.format(ano + 18))
elif idade == 18:
    print('Você tem {} anos está na epoca de se alistar.'.format(idade))
else:
    print('Você tem {} anos e já passou {} anos do tempo de se alistar.'.format(idade, idade - 18))
    print('Você deveria ter se alistado em {}.'.format(ano + 18))
