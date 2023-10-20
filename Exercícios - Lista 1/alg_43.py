import math

print('Calculadora de logarítimo na base 10\n-----------------------------')

num = int(input('Digite um número: '))
print(num)

logaritimo = math.log(num) / math.log(10)

print(f'\nLogarítimo de {num} é {int(logaritimo)}.')
