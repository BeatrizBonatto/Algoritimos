#numero:
#quadrado:
#raiz quadrada:
print('Calculadora de potencia e raiz quadrada\n---------------------------------------')

num = float(input('Digite o número que quer calcular: '))

pot_quad = float(num**2)
raiz_quad = float(num**(1/2))

print(f'Resultado:\nNúmero:{num:.2f}\nPotencia quadrada:{pot_quad:.2f}\nRaiz quadrada:{raiz_quad:.2f}')
