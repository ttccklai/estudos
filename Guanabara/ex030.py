n = int(input('digite um numero: '))
d = n % 2

if d == 0:
    print('o numero {} é par'.format(n))
else:
    print('o numero {} é impar'.format(n))