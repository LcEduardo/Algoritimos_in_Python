voted = {}

def verifica_eleitor(nome):
    if voted.get(nome): # get(Pegar) retornará um valor se nome já estiver na tabela hash
        print('Manda embora!')
    else:
        voted[nome] = True
        print('Deixe votar!')

while True:
    nome = input("Digite o nome (ou 'sair' para terminar): ")
    if nome.lower() == 'sair':
        break
    verifica_eleitor(nome)

print("Programa encerrado.")
