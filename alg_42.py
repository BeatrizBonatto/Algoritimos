import math

print('Calculadora trigonométrica\n-----------------------------')

entrada = float(input('Digite um Ângulo em graus: '))
print(entrada)

angulo = (entrada * 3.14)/180
sen = math.sin(angulo)
cos = math.cos(angulo)
tg = math.tan(angulo)
co_sec = 1/math.sin(angulo)
sec = 1/math.cos(angulo)
co_tg = 1/math.tan(angulo)

print('-----------------------------\n')
print(f'Seno: {sen:.2f}')
print(f'Co-seno: {cos:.2f}')
print(f'Tangente: {tg:.2f}')
print(f'Co-secante: {co_sec:.2f}')
print(f'Secante: {sec:.2f}')
print(f'Cotangente: {co_tg:.2f}')