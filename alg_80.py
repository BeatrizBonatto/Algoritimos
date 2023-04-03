print('\nLocadora de vídeo')

qnt_fita = int(input('\nDigite a quantidade de fitas: '))
val_aluguel = float(input('Digite o valor do aluguel: '))

fat_ano = (qnt_fita/3) * val_aluguel * 12
print(f'\nFaturamento anual: {fat_ano}')

multas = val_aluguel * 0.1 * (qnt_fita/3)/10
print(f'\nMultas mensais: {multas:.2f}')

qnt_final = (qnt_fita - (qnt_fita * 0.02) + (qnt_fita/10)) 
print(f'Quantidade de fitas no final do ano: {qnt_final:.2f}')