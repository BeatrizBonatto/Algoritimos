print('\nleia um valor de hora e informe quantos minutos se passaram desde o iníciõ do dia')

hora = int(input('\nentre com hora atual: '))
min = int(input('\nentre com minutos: '))

tempo = (hora * 60) + min

print(f'Até agora se passaram: {tempo} min')
