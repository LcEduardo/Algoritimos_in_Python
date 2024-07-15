# o grafo
grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

# a tabela de custos
infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

# a tabela de pais
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def encontrar_no_de_menor_custo(custos):
    menor_custo = float("inf")
    no_de_menor_custo = None
    # Percorre cada nó.
    for no in custos:
        custo = custos[no]
        # Se for o menor custo até agora e não foi processado ainda...
        if custo < menor_custo and no not in processados:
            # ... define como o novo nó de menor custo.
            menor_custo = custo
            no_de_menor_custo = no
    return no_de_menor_custo

# Encontra o nó de menor custo que você ainda não processou.
no = encontrar_no_de_menor_custo(custos)
# Se você processou todos os nós, este loop while está concluído.
while no is not None:
    custo = custos[no]
    # Percorre todos os vizinhos deste nó.
    vizinhos = grafo[no]
    for v in vizinhos.keys():
        novo_custo = custo + vizinhos[v]
        # Se for mais barato chegar a este vizinho passando por este nó...
        if custos[v] > novo_custo:
            # ... atualiza o custo para este nó.
            custos[v] = novo_custo
            # Este nó se torna o novo pai para este vizinho.
            pais[v] = no
    # Marca o nó como processado.
    processados.append(no)
    # Encontra o próximo nó a ser processado e repete o loop.
    no = encontrar_no_de_menor_custo(custos)

print("Custo do início para cada nó:")
print(custos)
