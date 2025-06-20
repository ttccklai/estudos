nome = input('Qual seu nome completo? ').strip()
nome_split = nome.split()
primeiro_nome = nome_split[0]
ultimo_nome = nome_split[-1]
print('seu primeiro nome é {} e ultimo sobrenome é {}'.format(primeiro_nome, ultimo_nome))