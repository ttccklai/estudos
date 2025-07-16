while True:
    n = int(input("Digete um numero para ver a tabuada: "))
    if n < 0:
        break
    print(f"Tabuada do {n}:")
    for tabuada in range(1, 11):
        print(f'{n} x {tabuada} = {n * tabuada}')
print("Programa encerrado.")