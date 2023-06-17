""" Calcula valor de uma passagem com base na distância e desconto """

distância = float(input('Digite a distância da viagem: '))

if distância <= 200:
	tarifa = 0.50
else:
	tarifa = 0.45

print(f'O valor da viagem ficará no valor de R${tarifa * distância :.2f}.')
