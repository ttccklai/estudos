import math

ang = float(input('digite um angulo: '))

seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print('o seno do angulo {} é: {:.2f}, o cosseno é: {:.2f} e a tangente é: {:.2f}'.format(ang, seno, cosseno, tangente))

# rd = radians(ang)

# print('o seno do angulo é: {}, o cosseno do angulo é: {} e a tangente do angulo é: {}'.format(sin(rd), cos(rd), tan(rd)))