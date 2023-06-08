""" Realiza alguas buscas dentro de uma string """

frase = input('Digite uma frase: ').strip().lower()

print(f'A letra A aparece {frase.lower().count("a")} vezes.')
print(f'A primeira vez que a letra A aparece é na posição {frase.find("a")+1}.')
print(f'A última vez que a letra A aparece é na posição {frase.rfind("a")+1}.')
