print('\nCalcular rendimento na poupança:\n')

p = float(input('Digite o valor da aplicação: '))
i = float(input('Digite a taxa (0 - 1): '))
n = float(input('Digite o número de meses: '))

va = p*(((1 + i )**n)-1) / i

print(f'\nO valor acomulado é R${va:.2f}')
