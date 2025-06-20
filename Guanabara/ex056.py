media_idade = 0
media = 0
mais_velho = 0
nome_mais_velho = ''
cont = 0

for pessoa in range(1, 5):
    print(f'----- {pessoa}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()  
    
    media_idade += idade
    media = media_idade / pessoa
    
    if idade > mais_velho:
        mais_velho = idade
        nome_mais_velho = nome
        
    if sexo == 'F' and idade < 20:
        cont += 1
    
print(f'A média de idade do grupo é {media:.2f} anos.')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_mais_velho}.')
print(f'Ao todo são {cont} mulheres com menos de 20 anos.')