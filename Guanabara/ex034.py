salario = float(input('Digite o salário: '))

if salario >=1250:
    aumento = salario * 0.1
    novo_salario = salario + aumento
else:
    aumento = salario * 0.15
    novo_salario = salario + aumento

print('Seu salario era de R${:.2f} e agora é de R$ {:.2f}'.format(salario, novo_salario))
print('O aumento foi de R$ {:.2f}'.format(aumento))