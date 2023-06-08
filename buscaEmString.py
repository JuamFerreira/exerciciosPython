""" Realiza algumas buscas dentro de uma string """

frase = input('Digite seu nome completo: ').strip()

print(f'A letra A aparece {frase.lower().count("a")} vezes.')
print(f'A primeira vez que a letra A aparece é na posição {frase.lower().find("a") + 1}.')
print(f'A última vez que a letra A aparece é na posição {frase.lower().rfind("a") + 1}.\n')

nome = frase.split()
print(f'Seu primeiro nome é {nome[0]}.')
print(f'Seu último nome é {nome[len(nome) - 1]}.')
