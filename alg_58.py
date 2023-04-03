import math

print('Entrar com valores para xnum 1, xnum2 e xnum3 e imprimir o valor de x, sabendo-se que:')
print('X = xnuml + ((xnum2) / (xnum3 + xnuml)) + 2(xnuml - xnum2) + log 64 na base 2\n')

num1 = float(input('Entre com 1 valor: '))
num2 = float(input('Entre com 2 valor: '))
num3 = float(input('Entre com 3 valor: '))
num4 = float(input('Entre com 4 valor: '))

x = num1 + (num2 / (num3 + num1)) + 2 *(num1 - num2) + math.log(64)/math.log(2)

print(f'\nX = {x:.2f}')