print('\nEntre com peso de uma pessoa, só a parte inteira, para calcular: ')
print('- O peso da pessoa em gramas;')
print('- Novo peso em gramas se a pessoa engordar 12%.\n')

peso = int(input('Entre com peso: '))

peso_gramas = peso * 1000
novo_peso = peso_gramas * 1.12

print(f'\nPeso em gramas: {peso_gramas}g\nNovo peso: {novo_peso:.2f}g')