def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

lista = [1, 2, 3, 4]
print(f'{soma(lista)}')
