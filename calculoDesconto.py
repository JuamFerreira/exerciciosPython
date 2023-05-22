valor = float(input('Digite um valor para calcular 5% de desconto: R$'))

print('O valor {}R$ com 5% de desconto passa a ser {:0.2f}'.format(valor, valor - (valor*5/100)))
