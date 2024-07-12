# Algoritimos em python

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

- ex01.py: é um modelo de empilhamento para executar as funções. 
- ex02.py: é um código recursivo para calular o fatorial. 

Para mais informações, acesse: [Medium.com](https://medium.com/@lucase.carvalho1704/recurs%C3%A3o-e-pilhas-43fcd1408a4a)