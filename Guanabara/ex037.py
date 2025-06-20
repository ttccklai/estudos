num = int(input('Digite um número: '))
print("""Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL""")
opcao = int(input('Sua opção: '))

#[2:] remove os dois primeiros caracteres da conversão do número
if opcao == 1:
    print('o numero {} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('o numero {} convertido para octal é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('o numero {} convertido para hexadecimal é igual a {}'.format(num, hex(num)))
else:
    print('Opção inválida. Tente novamente.')