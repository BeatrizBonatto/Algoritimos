print('\nSalário liquido de professor\n')

horas = float(input('Horas trabalhadas: '))
valor = float(input('Valor da hora-aula: '))
desc = float(input('Percentual de desconto: '))

sb = horas * valor
td = (desc / 100) * sb
sl = sb - td

print(f'\nSalario liquido: R${sl:.2f}')
