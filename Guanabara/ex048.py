s = 0
cont = 0
for impares in range(1, 501, 2):
    if impares % 3 == 0:
        s += impares
        cont = cont+ 1
print(f"A soma dos valores solicitados é {s}.")
print(cont)