import random

a1 = input('digite um nome: ')
a2 = input('digite outro nome: ')
a3 = input('digite mais um nome: ')
a4 = input('digite o último nome: ')

lista = [a1, a2, a3, a4]

escolhido = random.choice(lista)

print('O nome escolhido foi: {}'.format(escolhido))