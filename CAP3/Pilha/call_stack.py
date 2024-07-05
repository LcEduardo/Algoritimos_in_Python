def sauda(nome):
    print(f'Olá {nome}!')
    sauda2(nome)
    print(f'preparando para dizer tchau...')
    tchau()

def sauda2(nome):
    print(f'Como vai {nome}?')

def tchau():
    print(f'ok, tchau!')

sauda('Luffy')