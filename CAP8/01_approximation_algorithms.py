# Você passa uma lista, e ela é convertida para um conjunto.
estados_necessarios = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

estacoes = {}
estacoes["kone"] = set(["id", "nv", "ut"])
estacoes["ktwo"] = set(["wa", "id", "mt"])
estacoes["kthree"] = set(["or", "nv", "ca"])
estacoes["kfour"] = set(["nv", "ut"])
estacoes["kfive"] = set(["ca", "az"])

def meu_cobertor_de_conjuntos(estados_necessarios, estacoes):
    estacoes_finais = set()
    while estados_necessarios:
        melhor_estacao = None
        estados_cobertos = set()
        for estacao, estados_da_estacao in estacoes.items():
            cobertos = estados_necessarios & estados_da_estacao
            if len(cobertos) > len(estados_cobertos) and estacao not in estacoes_finais:
                melhor_estacao = estacao
                estados_cobertos = cobertos
        if melhor_estacao is not None:
            estados_necessarios -= estados_cobertos
            estacoes_finais.add(melhor_estacao)
            estacoes.pop(melhor_estacao)
        else:
            return None
    return estacoes_finais

print(meu_cobertor_de_conjuntos(estados_necessarios, estacoes))
