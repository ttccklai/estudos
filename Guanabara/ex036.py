emprestimo = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario? '))
anos = int(input('Em quantos anos você quer pagar? '))

prestacao = (emprestimo / anos) / 12
minimo = salario * 0.3

print('Para pagar uma casa de R${:.2f} em {} anos'.format(emprestimo, anos))
print('A prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo aprovado')
else:
    print('Emprestimo negado')