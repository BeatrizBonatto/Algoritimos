print('Calculadora de Perímetro, Área e Diagonal de Quadrado\n')

lado = float(input('Digite o comprimento do lado(cm):'))

perimetro = 4 * (lado)
area = lado**2
diagonal = lado * (2**(1/2))

print(f'Perímetro:{perimetro:.2f}cm\nÁrea:{area:.2f}cm²\nDiagonal:{diagonal:.2f}cm')
