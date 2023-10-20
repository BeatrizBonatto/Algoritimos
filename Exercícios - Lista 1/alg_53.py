print('Calculadora de diagonal de Paralelepípedo')

base = float(input('Digite o comprimento da base:'))
altura = float(input('Digite o comprimento da altura:'))
profund = float(input('Digite o comprimento da profundidade:'))

diagonal = ((base**2)+(altura**2)+(profund**2))**(1/2)

print(f'Diagonal do Paralelepípedo:{diagonal:.2f} cm')
