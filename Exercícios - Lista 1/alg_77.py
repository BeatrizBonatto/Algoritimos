print('\nLer dois números reais e imprimir (num1 - num2)² e a (num1)² - (num2)²\n')

a = float(input('\nDigite 1° número: '))
b = float(input('\nDigite 2° número: '))

d = (a - b)**2
q = (a**2) - (b**2)

print(f'\nResultados:\n(num1 - num2)²= {d}\n(num1)² - (num2)²= {q}')
