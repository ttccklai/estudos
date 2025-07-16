n = int(input('Digite um numero: '))
aceite = input('Quer continuar? [S/N] ').strip().upper()[0]
c = media = 0 

while aceite != "S":
    c += 1
    media += n
    aceite = input('Quer continuar? [S/N] ').strip().upper()[0]
    if aceite == 'S':
        n = int(input('Digite um numero: '))
    else:
        print('Opção inválida! Digite S ou N.')
        
media /= c
print(f'Você digitou {c} números e a média foi {media:.2f}.')