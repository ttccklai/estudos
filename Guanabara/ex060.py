# fatorial = int(input("Digite um número inteiro positivo para o calculo fatorial: "))
# cont = fatorial
# while cont > 0:
#     # fatorial = fatorial * (fatorial - 1)
#     print(cont)
#     cont -= 1
#     fatorial *= cont
# print(f"O fatorial do número digitado é: {fatorial}")


num = int(input("Digite um número inteiro positivo para o cálculo fatorial: "))
c = num
fatorial = 1

print(f"Calculando {num}! = ", end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(fatorial)