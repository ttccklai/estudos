n = int(input("Digite um numero [999 para parar]: "))
c = 0
soma = 0
while n != 999:
    soma += n
    c += 1
    n = int(input("Digite um numero [999 para parar]: "))
    
print(f"A soma dos {c} valores foi {soma}.")