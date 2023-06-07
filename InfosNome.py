""" O programa é responsável por capturar um nome e extrair algumas informações relevantes sobre ele."""

nome = input('Digite seu nome completo: ')

print(f'Seu nome maiúsculo {nome.upper()};')
print(f'Seu nome minúsculo {nome.lower()};')

nome_separado = nome.split()

print(f'Seu nome tem, ao todo, {len("".join(nome_separado))} letras;')
print(f'Seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])} letras.')
