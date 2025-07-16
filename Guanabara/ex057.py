# s = ""

# while s != "M" and s != "F":
#     s = str(input("Digite seu sexo [M/F]: ")).upper()
#     print("Opção inválida! Tente novamente.")
# if s == "M":
#     print("Seu sexo é Masculino")
# elif s == "F":
#     print("Seu sexo é Feminino")

sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input("Dados invalidos. Digite seu sexo [M/F]: ")).strip().upper()[0]

print(f"Sexo {sexo} registrado com sucesso.")