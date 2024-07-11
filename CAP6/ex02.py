# implementando o algoritimo

from collections import deque

def pessoa_e_vendedora(nome):
    return nome[-1] == 'y'

grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

def buscar(nome):
    fila_de_busca = deque()
    fila_de_busca += [nome]
    # É assim que você rastreia quais pessoas você já pesquisou antes.
    verificadas = set()
    while fila_de_busca:
        pessoa = fila_de_busca.popleft()
        # Só pesquisa essa pessoa se você ainda não a pesquisou.
        if pessoa in verificadas:
            continue
        if pessoa_e_vendedora(pessoa):
            print(pessoa + " é um vendedor de mangas!")
            return True
        fila_de_busca += grafo[pessoa]
        # Marca essa pessoa como pesquisada
        verificadas.add(pessoa)
    return False

buscar("voce")
