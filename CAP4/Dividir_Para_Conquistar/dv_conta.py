def conta(lista):
    if lista ==[]:
        return 0
    
    return 1 + conta(lista[1:])
     
lista = [1, 2, 3, 4]
print(f'{conta(lista)}')
