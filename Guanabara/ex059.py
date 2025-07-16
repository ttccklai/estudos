import time

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

opcao = int(input("""escolha uma opção:\n
                1: Somar\n
                2: Multiplicar\n
                3: Maior\n
                4: Novos números\n
                5: Sair do programa\n"""))

while opcao != 5:
    if opcao == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} e {n2} é {soma}.")
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f"A multiplicação entre {n1} e {n2} é {multiplicacao}.")
    elif opcao == 3:
        if n1 > n2:
            print(f"O maior número é {n1}.")
        elif n2 > n1:
            print(f"O maior número é {n2}.")
        else:
            print("Os números são iguais.")
    elif opcao == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    else:
        print("Opção inválida. Tente novamente.")
    opcao = int(input("""escolha uma opção:\n
                1: Somar\n
                2: Multiplicar\n
                3: Maior\n
                4: Novos números\n
                5: Sair do programa\n"""))
print("finalizando o programa...")
time.sleep(2)
print("Obrigado por usar o programa!")
print("Programa encerrado. Até mais!")