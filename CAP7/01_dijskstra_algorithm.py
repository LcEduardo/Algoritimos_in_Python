# Todas são tabelas hashs.


grafo = {}
grafo["inicio"]= {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

# Tabelha hash para custos.

infinito = float("inf")
custos = {}

custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

# Tabela hash dos pais.

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

# array para registro
processados = []
print(f'{grafo["inicio"]}')
print(f'{grafo["fim"].keys()}')