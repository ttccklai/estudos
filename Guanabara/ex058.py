import random 

numero = random.randint(1, 10)

print("Acabei de pensar em um número entre 1 e 10. Tente adivinhar!")

# tentativas = 0
# chute = int(input('Digite seu palpite: '))

# while numero != chute:
#     if numero > chute:
#         chute = int(input('Mais. tente novamente: '))
#     if numero < chute:
#         chute = int(input('Menos. tente novamente: '))
#     tentativas += 1
# print(f"Parabéns! Você acertou o número {numero} em {tentativas +1} tentativas.")


acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Digite seu palpite: "))
    palpites += 1
    
    if jogador == numero:
        acertou = True
    else:
        if jogador < numero:
            print("Mais... Tente novamente.")
        else:
            print("Menos... Tente novamente.")
print(f"Parabéns! Você acertou o número {numero} em {palpites} tentativas.")