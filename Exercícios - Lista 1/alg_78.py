print('\nDado um polígono convexo de n lados, podemos calcular o número de diagonais diferentes')
print('fórmula : nd = n (n —3)/ 2.\n')

n = int(input('DIgite o número de lados do polígono: '))

nd = n * (n - 3) / 2

print(f'\nNúmero de diagonais: {nd}')
