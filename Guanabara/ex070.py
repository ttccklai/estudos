total = c = 0

while True:
    
    material = str(input("Digite o nome do material: "))
    valor = float(input("Digite o valor do material: "))
    c += 1
    
    if c == 1 or valor < menor:
        menor = valor
        nome_menor = material
    # else:
    #     if valor < menor:
    #         menor = valor
    #         nome_menor = material
        
    total += valor
    
    if valor > 1000:
        totmil += 1
    
    continua = ' '
    while continua not in 'SN':
        continua = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
        
    if continua == "N":
        break
    
print(f'-' * 20 + ' FIM DO PROGRAMA ' + '-' * 20)
print(f"Total gasto na compra: R${total:.2f}")
print(f"Quantidade de materiais que custam mais de R$1000: {totmil}")
print(f"Material mais barato: {nome_menor} que custa R${menor:.2f}")