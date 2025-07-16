numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'batata')

while True:
    num = int(input(f'Digite um numero entre 0 e 10: '))
    
    if num >= 0 and num <= 10:
        break
    print('Tente novamente. ', end='')
    
    
print(f'Você digitou o número {numeros[num]}.')
        