print('\nPrestação em atraso, fórmula: prestação = valor + (valor*(taxa/100)*tempo). ')

valor = int(input('\nDigite o valor da prestação: '))
taxa = int(input('Digite a taxa: '))
tempo = int(input('Digite o tempo (meses): '))

prestacao = valor + (valor * (taxa/100) * tempo)

print(f'\nO valor da prestacao em atraso é R${prestacao:.2f}')