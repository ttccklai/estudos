num = int(input('Digite um número: '))
cont = 0 

for n in range(1, num + 1):
    # o resto da divisão só vai dar zero se o numero for primo (divisivel por 1 e por ele mesmo)
    if num % n == 0:
        print(f'\033[33m{n}')
        cont += 1
    else:
        print(f'\033[31m{n}')

print(f'O número {num} foi divisível {cont} vezes.')
if cont == 2:   
    print(f'Por isso o numero {num} é PRIMO')
else:
    print(f'Por isso o número {num} não é PRIMO')