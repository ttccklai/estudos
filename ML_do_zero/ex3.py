M1 = float(input("Nota 1: "))
M2 = float(input("Nota 2: "))
M3 = float(input("Nota 3: "))

media = (M1 + M2 + M3) / 3

if media >= 0.0 and media <= 4.0:
  print("reprovado")
elif media > 4.0 and media < 6.0:
  exame = float(input("valor da nota do exame: "))
  if exame >= 6.0:
    print("aprovado no exame")
  else:
    print("reprovado no exame")
elif media >= 6.0:
  print("aprovado")