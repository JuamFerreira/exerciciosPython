nome = str(input('Qual seu nome? '))
if nome.lower() == 'juam':
    print('Nome maravilhoso hein!')
elif nome.lower() == 'pedro' or nome.lower() == 'maria' or nome.lower() == 'paulo':
    print('Que nome normalzinho!')
elif nome.lower() in 'Ana Claudia Amanda Geovandia Paula':
    print('Você tem um nome feminino')
elif nome.lower() == 'janine':
    print('O amor da minha Vida!!!')
else:
    print('Um nome ok')
print(f'Tenha um bom dia {nome}!')
