c_idade_maior = c_idade_menor = c_homens = c_mulheres = 0

while True:
    print("-" * 30)
    print("CADASTRE UMA PESSOA")
    print("-" * 30)
    
    idade = int(input("Idade: "))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    
    if idade >= 18:
        c_idade_maior += 1
    else:
        c_idade_menor += 1
        
    if sexo == 'M':
        c_homens += 1
    if sexo == 'F':
        c_mulheres += 1
    
    continua = ' '
    while continua not in 'SN':
        continua = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
        
    if continua == "N":
        break

print(f"Total de pessoas com mais de 18 anos: {c_idade_maior}")
print(f"Total de pessoas com menos de 18 anos: {c_idade_menor}")
print(f"Total de homens cadastrados: {c_homens}")
print(f"Total de mulheres cadastradas: {c_mulheres}")
print("Programa encerrado.")
