#Fazer um algoritmo que possa entrar com o saldo de uma aplicação e imprima o novo saldo, considerando o reajuste de 1%.

print('Houve um reajuste de saldo de 1% neste mês\n')

saldo_atual = float(input('Para consulta, digite seu saldo atual: R$'))


saldo_reaj = saldo_atual*1.01

print(f'\nSeu novo saldo é R${saldo_reaj:.2f}')
