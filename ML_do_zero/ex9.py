dict = {}

for aluno in range(1, 4):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))
    dict[nome] = nota
    
print(dict)

soma = 0

for nota in dict.values():
    soma += nota
    media = soma / len(dict)
    
print(f'A média das notas é: {media:.2f}')