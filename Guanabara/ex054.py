maior = 0
menor = 0

for idade in range(1, 7):
    ano = int(input(f'Em que ano a {idade}ª pessoa nasceu? '))
    
    idade_atual = 2025 - ano
    print(idade_atual)
    
    if idade_atual >= 18:
        maior += 1
    else:
        menor += 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade e {menor} pessoas menores de idade.')