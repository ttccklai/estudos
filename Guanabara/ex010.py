import math

num = float(input('Digite um valor: '))
print('o valor digitado foi: {} e o valor inteiro é: {}'.format(num, int(num)))
print('O valor digitado foi: {} e a sua porção inteira é: {}'.format(num, math.trunc(num)))