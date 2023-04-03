#o valor em reais de cada quilowatt
#o valor em reais a ser pago;
#o novo valor a ser pago por essa residência com um desconto de 10%.
print('Calculadora de conta de luz\n-------------------------------------------------------')

salario_min = float(input('Digite o salário mínimo: R$'))
kw = float(input('Digite a quantidade de quilowatt: '))

preco = salario_min / 700
valor_pago = preco * kw
valor_desco = valor_pago * 0.9

print(f'\nPreço do quilowatt é R${preco:.2f};\nValor a ser pago: R${valor_pago:.2f}\nValor com desconto de 10%: R${valor_desco:.2f}')