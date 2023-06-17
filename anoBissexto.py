""" Analisa se o ano digitado é bissexto """
from datetime import date

ano = int(input('Digite o ano a analisar, ou 0 para o ano atual: '))

if ano == 0:
	ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print(f'O ano de {ano} é BIssexto!')
else:
	print(f'O ano de {ano} NÃO é BIssexto!')
