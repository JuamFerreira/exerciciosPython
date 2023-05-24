from math import radians, sin, cos, tan

ângulo = float(input('Digite o ângulo desejado: '))

seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))

print(f'O ângulo de {ângulo}° \n'
      f'Tem o seno de {seno:.2f} \n'
      f'O cosseno de {cosseno:.2f} \n'
      f'E a tangente de {tangente:.2f}')
