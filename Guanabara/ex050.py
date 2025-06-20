s = 0

for num in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos valores pares é {s}.')