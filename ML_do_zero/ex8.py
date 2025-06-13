l = []

for item in range(1, 6):
  print(item)
  l.append(item)
  print(l)

soma = 0

for item in l:
  soma = soma + item
  print(soma)
  
# ou 
# for item in range(len(l)):
#   soma = soma + l[item]

# ou 
# np.array(l).sum()