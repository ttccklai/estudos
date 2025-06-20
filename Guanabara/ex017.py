import math

ca = float(input('Digite um valor para o cateto adjacente: '))
co = float(input('Digite um valor para o cateto oposto: '))
hi = (ca ** 2 + co ** 2) ** (1/2)
print('A hipotenusa mede: {:.2f}'.format(hi))

hypot = math.hypot(ca, co)
print('A hipotenusa mede: {:.3f}'.format(hypot))