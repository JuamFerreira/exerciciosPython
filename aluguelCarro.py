dias = int(input('Quantidade de dias alugado: '))
km = float(input('Quantidade de quilometros rodados: '))

valor_final = dias * 60 + km * 0.15

print('O valor total do aluguél é R${:.2f}'.format(valor_final))
