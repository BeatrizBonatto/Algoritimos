import math

print('Calculadora de logarítimo na base 10\n-----------------------------')

num = int(input('\nDigite um número para se descobrir o log: '))
print(num)

base = int(input('\nDigite a base do calculo: '))
print(base)

logaritimo = math.log(num) / math.log(base)

print(f'O logarítimo de {num} na base {base} é {logaritimo:.2f}.')