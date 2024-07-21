# Algoritmos em python

Baseado no livro **Entendendo Algoritmos** de *Aditya Y.Bhargava*.

## Prefácio:

 1. CAP1 - Pesquisa binária
 2. CAP2 - Ordenação por seleção
 3. CAP3 - Recursão
    1. Recursão
    2. Pilha
4. CAP4 - Quicksort
    1. Dividir para conquistar
    2. Quicksort
5. CAP5 - Tabela hash
6. CAP6 - Pesquisa em largura
    1. Grafos
    2. Filas 
7. CAP7 - Algoritmo de Dijkstra
    1. Grafos Ponderados
8. CAP8 - Algoritmos Gulosos
    1. Algoritmo de aproximação
    2. NP-completos
9. CAP9 - Programação dinâmica
    1. Maior substring comum
    2. Maior subsquência comum


## CAP1: Pesquisa Binária

**Exemplo:** temos números de 1 a 100 e eu peço para você adivinhar um número. O que você faria?

Você provavelmente começaria chutando 50, porque, se não for esse o número, você pode descobrir se o número é maior ou menor que 50, eliminando assim metade dos números restantes. Você continuaria esse processo até acertar o número.

Para mais informações acesse: [Medium.com](https://medium.com/@lucase.carvalho1704/pesquisa-bin%C3%A1ria-8a1179875d63)

## CAP2: Ordenaão Por Seleção

Exemplo: Pense em uma lista de frutas, onde cada fruta tem sua quantidade. Por exemplo, morango tem 3, banana tem 4, maçã tem 1, e assim por diante. As frutas estão na lista de forma desorganizada e precisamos ordená-las para facilitar a pesquisa.

Para isso, percorremos toda a lista e verificamos qual fruta tem a menor quantidade, adicionando-a a uma nova lista. Repetimos esse processo até que todas as frutas estejam ordenadas. Esse é o algoritmo de ordenação por seleção. Seu tempo de execução é $O(n^2)$, embora a lista diminua conforme as execuções. 

## CAP3: Recursão

Aprendemos sobre Recursão, que é uma técnica poderosa. Basicamente, a função chama a si mesma, dividindo-se em caso base e caso recursivo.

Nesse capítulo, também analisamos uma estrutura de dados que é muito útil em casos de recursão: a Pilha. Ela ajuda bastante no controle de execução das funções (pilha de chamada).

Uma pilha é como uma lista de passos que devemos seguir. Pense que cada passo é empilhado um sobre o outro. O passo que estiver no topo será executado primeiro, seguido pelo próximo passo. Observe que a pilha segue o modelo LIFO (Last In, First Out). 

Para mais informações, acesse: [Medium.com](https://medium.com/@lucase.carvalho1704/recurs%C3%A3o-e-pilhas-43fcd1408a4a)

## CAP4: Quicksort

É um algoritmo que ordena uma lista ou array. Embora seja similar à ordenação por seleção, é mais eficaz, pois utiliza a técnica de divisão e conquista, que é muito útil para otimizar o processo de ordenação.

 - **01_sum_recursive.py e 02_count_recursive.py:** demonstram como recursão se encaixa nessa técnica.

 - **03_quicksort.py:** demonstra o funcionamento.

Para mais informações, acesse: [Medium.com](https://medium.com/@lucase.carvalho1704/recursão-e-pilhas-43fcd1408a4a)

## CAP5: Tabela Hash

Tabelas hash são estruturas de dados que armazenam pares de chave-valor usando uma função hash para calcular o índice de armazenamento no array. Isso permite uma recuperação de dados rápida, com complexidade média de O(1) para operações de busca, inserção e exclusão, se a função hash distribuir as chaves uniformemente. Problemas como colisões podem ocorrer quando duas chaves geram o mesmo índice, mas podem ser resolvidos com técnicas como encadeamento e endereçamento aberto. Apesar desses desafios, tabelas hash são amplamente usadas em aplicações devido à sua eficiência e alto desempenho.

 - **01_function_hash.py:** como criar uma tabela hash em py
 - **02_function_hash.py:** outra maneira de declarar tabela hash.
 - **03_fruit_hash_tables.py:** exemplo prático.
 - **04_check_voter.py:** exemplo prático.

 Para mais informações acesse: [Medium.com](em criação)
