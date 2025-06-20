n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print('o numero {} é maior que {} e {}'.format(n1, n2, n3))
elif n2 > n1 and n2 > n3:
    print('o numero {} é maior que {} e {}'.format(n2, n1, n3))
else:
    print('o numero {} é maior que {} e {}'.format(n3, n1, n2))