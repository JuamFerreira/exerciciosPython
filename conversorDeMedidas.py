# Converte valor em metro para outras medidas possíveis.
medida = float(input("digite a medida em metros: "))

print(f'A medida de { medida }m corresponde a: \n'
      f'{ medida / 1000 }km \n'
      f'{ medida / 100 }hm \n'
      f'{ medida / 10 }dam \n'
      f'{ medida * 10 }dm \n'
      f'{ medida * 100 }cm \n'
      f'{ medida * 1000 }mm')
