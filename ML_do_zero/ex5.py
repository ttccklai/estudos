numero = 1
soma = 0

while numero <= 5:
  nota = int(input("Digite a nota: "))
  soma = nota + soma
  numero = numero + 1

print("a media é ", soma / 5)