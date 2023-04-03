print('\nCriar um algoritmo que receba um número real, calcular e imprimir:')
print('\n- a parte inteira do número')
print('\n- a parte fracionária do número')
print('\n- o número arredondado.')

num = float(input('\nentre com um numero com parte fracionaria: '))

num_i = int(num - 0.5)
num_fra = num - num_i
num_a = int(num + 0.00001)

print(f'\nParte inteira: {num_i}')
print(f'Parte fracionária: {num_fra:.3f}')
print(f'Número arredondado: {num_a}')