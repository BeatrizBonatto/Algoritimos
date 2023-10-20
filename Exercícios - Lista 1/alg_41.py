print('\nCalculadora de média ponderada\n----------------------------------')

num1 = int(input('\nDigite a nota 1:'))
num2 = int(input('\nDigite a nota 2:'))
num3 = int(input('\nDigite a nota 3:'))
num4 = int(input('\nDigite a nota 4:'))

med_pond = int(((num1*1)+(num2*2)+(num3*3)+(num4*4))/10)

print(f'\n----------------------------------\nMédia ponderada:{med_pond}')
