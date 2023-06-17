""" Informa o valor da multa por km excedido """

velocidade = float(input('Digite a velocidade do veículo: '))

if velocidade > 80:
	print(f'''\tVocê excedeu o limite de velocidade de 80km/h
	Por estar na velocidade de {velocidade}km/h pagará a seguinte multa:
	R${(velocidade - 80) * 7 :.2f}''')
else:
	print('Limite de velocidade respeitado!')
