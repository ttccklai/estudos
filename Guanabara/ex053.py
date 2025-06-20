frase = str(input('Digite uma frase: '))
# frase = frase.replace(' ', '')
# frase = frase.lower()
frase = frase.strip().lower()
palavras = frase.split() # separa a frase pelos espaços em branco e cria uma lista de palavras
junto = ''.join(palavras) # junta as palavras da lista palavras pelo valor indicado antes do ponto
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    print(junto[letra])
    # é como se fosse um contador que começa do último índice da string e vai até o primeiro
    inverso += junto[letra]

print(f'O inverso de {junto} é {inverso}.')

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')