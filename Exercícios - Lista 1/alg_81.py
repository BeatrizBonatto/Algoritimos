print(f'\nVerificador da conta\n')

conta = int(input('Digite conta de três digitos: '))

d1 = (conta//100)
d2 = (conta % 100) // 10
d3 = conta % 100 % 10

inv = (d3 * 100) + (d2 * 10) + d1
soma = conta + inv

x1 = (soma//100) * 1
x2 = ((soma % 100) // 10) * 2
x3 = (soma % 100 % 10) * 3

digito = (x1 + x2 + x3) % 10
print(f'\nDigito verificados: {int(digito)}')
