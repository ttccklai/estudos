frase = input('Digite uma frase: ').strip()

print('O "a" aparece {} vezes e o "e" aparece {} vezes'.format(frase.count('a'), frase.count('e')))
print('O primeiro "a" aparece na posição {} e o primeiro "e" aparece na posição {}'.format(frase.find('a') + 1, frase.find('e') + 1))
print('O ultimo "a" aparece na posição {} e o ultimo "e" aparece na posição {}'.format(frase.rfind('a') + 1, frase.rfind('e') + 1))