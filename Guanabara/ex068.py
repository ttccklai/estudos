import random

# c = 0 

# while True:
#     num = int(input("Digite um número: "))
#     par_impar = str(input("Voce quer par ou impar [P/I]: "))
#     comp = random.randint(1,10)
#     soma = num + comp 
#     resto = soma % 2
#     c += 1
#     if resto == 0 and par_impar == 'P':
#         print(f"A soma de {num} com {comp} deu {soma}. {soma} é um numero PAR. Você acertou!")
#     elif resto != 0 and par_impar == 'I':
#         print(f"A soma de {num} com {comp} deu {soma}. {soma} é um numero IMPAR. Você acertou!")
#     elif resto == 0 and par_impar == 'I':
#         print(f"A soma de {num} com {comp} deu {soma}. {soma} é um numero PAR.")
#         break
#     elif resto != 0 and par_impar == 'P':
#         print(f"A soma de {num} com {comp} deu {soma}. {soma} é um numero IMPAR.")
#         break
    
# print(f"VOCÊ PERDEU")
# print(f"seu numero de tentivas foi {c}")

v = 0
print("Vamos jogar Par ou Ímpar!")
while True:
    jogador = int(input("Digite um número: "))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()[0]
    
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total}.")
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    
    if tipo == "P":
        if total % 2 == 0:
            print(f"Você VENCEU!")
            v += 1
        else:
            break
    if tipo == "I":
        if total % 2 != 0:
            print(f"Você VENCEU!")
            v += 1 
        else:
            break
    print("Vamos jogar novamente...")
    
print("Você PERDEU!")
print(f"seu número de vitorias foi {v}")