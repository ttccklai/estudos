nota = 0
soma = 0

for nota in range(1, 6):
  nota = int(input("Digite a nota: "))
  soma = soma + nota

media = soma / 5
print(media)