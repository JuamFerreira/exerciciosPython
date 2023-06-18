""" Programa que avalia a viabilidade de um financiamento imobiliário de acordo com valor do salário. """

vl_imovel = float(input('Informe o valor do imóvel: R$'))
salário = float(input('Informe o valor do seu salário: R$'))
tempo = int(input('Quantos anos parcelará o financiamento? '))

prestação = vl_imovel / (tempo * 12)
margem_segurança = salário * 0.30

print(f'O valor da prestação mensal para pagamento em {tempo} anos, é R${prestação :.2f}')

if prestação <= margem_segurança:
	print('Empréstimo APROVADO!')
else:
	print('Empréstimo NEGADO!')
print(f'Valor das parcelas equivale à {prestação / salário * 100 :.2f}% do seu salário.') # Retorna a porcentagem em relação ao salário
