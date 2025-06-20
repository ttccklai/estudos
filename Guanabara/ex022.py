nome = input('digite seu nome: ')

print('seu nome em maiusculo: {}'.format(nome.upper()))
print('seu nome em minusculo: {}'.format(nome.lower()))
print('seu nome tem {} letras com espaços'.format(len(nome)))
print('seu nome tem {} letras sem espaços'.format(len(nome) - nome.count(' ')))
