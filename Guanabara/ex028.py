from random import randint

computador = randint(0,5)
pessoa = int(input('Qual numero entre 0 e 5 você pensou? '))

if computador == pessoa:
    print('você acertou')
else:
    print('você errou')

print('o numero que pensei foi {}'.format(computador))