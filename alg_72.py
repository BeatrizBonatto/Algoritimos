print('\nDeposito, Calcular e imprimir o valor do rendimento e o valor total depois do rendimento.\n')

deposito = float(input('\nEntre com depósito: '))
taxa = float(input('Entre com a taxa de juros: '))

valor = (deposito * taxa) / 100
total = deposito + valor

print(f'\nRendimentos: R${valor:.2f}\nTotal: R${total}')