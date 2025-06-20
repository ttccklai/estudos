t1 = float(input('Digite o valor do primeiro segmento: '))
t2 = float(input('Digite o valor do segundo segmento: '))
t3 = float(input('Digite o valor do terceiro segmento: '))

if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')