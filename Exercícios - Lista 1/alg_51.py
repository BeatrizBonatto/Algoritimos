import math

print('Calculadora de Perímetro e Área de Circunferencia')

raio = float(input('Digite o valor do raio(cm):'))

perimetro = 2 * math.pi * raio
area = math.pi * (raio ** 2)

print(f'Perímetro:{perimetro:.2f}cm\nÁrea:{area:.2f}cm²')
