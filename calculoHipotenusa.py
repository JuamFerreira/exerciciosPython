import math

co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
print(f'O comprimento da hiputenusa é: { math.hypot(co, ca) :.2f }')



# # Sem precisar de importação
# cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
# cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
#
# hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
#
# print(f'O valor da hipotenusa é {hipotenusa:.2f}')
