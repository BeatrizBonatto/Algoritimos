print('\nEntre com número entre O e 60 e vou mostrar seu sucessor, sabendo que o sucessor de 60 é 0\n')

num = int(input('Digite número: '))

print('\nSucessor: ', (num + 1) % 61)
