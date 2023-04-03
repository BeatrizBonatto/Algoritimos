print('\nEntrar com os valores dos catetos de um triângulo retângulo e imprimira hipotenusa\n')

cat1 = float(input('Entre com 1° cateto: '))
cat2 = float(input('Entre com 2° cateto: '))

hip = ((cat1**2) + (cat2**2))** (1/2)

print(f'Hipotenusa: {hip:.2f}')