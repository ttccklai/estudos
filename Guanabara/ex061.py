termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

c = 1

while c <= 10:
    print(f"{termo}",end=' ')
    print(" -> " if c < 10 else " -> FIM", end='')
    termo += razao
    c += 1