import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

soma = 0

# primeiro ele acessa a linha, depois a coluna da matriz
for linha in range(matriz.shape[0]):
  for coluna in range(matriz.shape[1]):
    soma = soma + matriz[linha][coluna]
    print(soma)