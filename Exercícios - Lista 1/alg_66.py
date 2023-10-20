print('\nSabendo que o carro faz 12 km com um litro, quantos litros de combustível ele gastara em uma viagem.')

tempo = float(input('\nDigite o tempo gasto: '))
velocidade = float(input('Digite a velocidade média: '))

distancia =  tempo * velocidade
litros = distancia / 12

print(f'\nVelocidade= {velocidade}')
print(f'Tempo= {tempo}')
print(f'Distância= {distancia}')
print(f'Litros= {litros:.2f}')
