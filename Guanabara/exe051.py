primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(1, 11):
    pa = primeiro_termo + (i - 1) * razao
    print(pa, end=' -> ')
    # print('-> ' if i < 10 else 'FIM')
    # print('->')
print('FIM')