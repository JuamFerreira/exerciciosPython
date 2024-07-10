"""
    Sistema que simula um gateway de pagamento com descontos e acrescimo de júros
    com base no método de pagamento escolhido.
"""

print(f'{" Loja do Juam ":~^40}')   # Acrescenta uma formatação de preenchimento no texto

valor_total = float(input('Valor total da compra: '))
print('''FORMAS DE PAGAMENTO
      [ 1 ] à vista no Dinheiro/Cheque
      [ 2 ] à vista no cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual será a forma de pagamento? '))

match opção:
    case 1:
        valor_final = valor_total - (0.10 * valor_total)
    case 2:
        valor_final = valor_total - (0.05 * valor_total)
    case 3:
        valor_final = valor_total
        print(f'Sua compra será parcelada em 2x de R${valor_total / 2:.2f} SEM JUROS.')
    case 4:
        qtd_parcelas = int(input('Quantidade de parcelas: '))

        valor_final = valor_total * 0.20 + valor_total
        valor_parcelas = valor_final / qtd_parcelas

        print(f'Sua compra será parcelada em {qtd_parcelas}x de R${valor_parcelas:.2f} COM JUROS.')
    case _:
        print('\n OPÇÃO INVÁLIDA, TENTE NOVAMENTE \n')
        valor_final = valor_total

print(f'Sua compra de R${valor_total:.2f} vai custar R${valor_final:.2f}')
