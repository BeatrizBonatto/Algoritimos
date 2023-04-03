print('Calculadora de Perímetro, Área e Diagonal de Retângulo\n')

base = float(input('Digite o comprimento da base(cm):'))
altura = float(input('Agora digite o da altura(cm):'))

perimetro = 2*(base + altura)
area = base * altura
diagonal = (base**2 + altura**2)**(1/2)

print(f'Perímetro:{perimetro:.2f}cm\nÁrea:{area:.2f}cm²\nDiagonal:{diagonal:.2f}cm')