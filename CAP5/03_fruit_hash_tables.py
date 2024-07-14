frutas = {}

while True:
    chave = input('Digite o nome da fruta (ou "sair" para terminar): ')
    if chave == 'sair':
        break
    valor = input(f'Digite o valor da fruta {chave}: ')
    frutas[chave] = valor
    print(f'Dicionário atualizado: {frutas}')

print(f'Dicionário final: {frutas}')

while True:
    chave = input("Digite a chave para consultar o valor (ou 'sair' para terminar): ")
    if chave == 'sair':
        break
    if chave in frutas:
        print(f"O valor para a fruta '{chave}' é: {frutas[chave]}")
    else:
        print(f"A fruta '{chave}' não foi encontrada no dicionário.")
