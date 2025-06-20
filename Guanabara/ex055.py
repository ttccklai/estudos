maior_peso = 0
menor_peso = 100

for peso in range(1, 6):
    peso_atual = float(input(f'Peso da {peso}ª pessoa: '))
    if peso_atual > maior_peso:
        maior_peso = peso_atual
    if peso_atual < menor_peso:
        menor_peso = peso_atual
        
print(f'O maior peso lido foi {maior_peso}kg.')
print(f'O menor peso lido foi {menor_peso}kg.')