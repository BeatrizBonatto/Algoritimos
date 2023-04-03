import math

print('\nCálculo de volume de lata de óleo\nVolume = 3.14159 * R2 * altura.')

altura = float(input('\nDigite a altura da lata: '))
raio = float(input('Digite o raio da lata: '))

volume = math.pi * (raio**2) * altura


print(f'O volume da lata é: {volume:.2f}')