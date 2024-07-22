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

 ## CAP6: Pesquisa Em Largura

 **Pesquisa em largura** é um algoritmo que resolve problemas de *caminho mínimo* utilizando **grafos**.

### Como assim caminhos mínimos?

**Por exemplo:** queremos sair da cidade A para cidade D.

![[grafos1 1.png]]

Nesse exemplo, podemos observar que existe dois caminhos. A pesquisa em largura encontrará o menor caminho que tem 2 caminhos apenas. Isso é caminho mínimo, entendendo isso podemos observar que toda a modelagem é feita por **grafos**.

### O que é Grafos?

Um modelo de grafos é um conjunto de *conexões*. 

**Por exemplo:** Eu devo dinheiro para o Arthur, que deve dinheiro para o Luiz, e o Andrei deve dinheiro para o Luiz.

![[grafos1.png]]

Com grafos temos um modelo para representar quem deve dinheiro a quem. Assim, ele fornece uma maneira de modelar como eventos diferentes estão conectados entre si. 

![[grafos3.png]]

Observe que os grafos são formados por vértices e arestas. Um vértice pode se conectar a muitos outros vértices e esses são chamados de vizinhos. Luiz é vizinho de Arthur, mas não é vizinho meu. 

### Mas como funciona a pesquisa em largura?

Primeiro fazemos duas perguntas:

- Existe um caminho do vértice A para o vértice B?
- Qual o caminho mínimo do vértice A até o B?

**Pensamos o seguinte:** estamos em uma cidade A e queremos chegar a cidade G. Verificamos os vizinhos da cidade A para analisar se um deles é a cidade G.

![[ex1.png]]

Percebemos que nenhuma delas são G. Então, verificamos os vizinhos dos vizinhos. 

![[ex2.png]]

Ainda não encontramos. Então continuamos a busca até achar um caminho. Essa é a primeira pergunta.

![[ex4.png]]

**A segunda pergunta é:** "Qual é o caminho mínimo?" Observe que encontramos primeiro as cidades B e C e depois as cidades D, E e J, e assim por diante. Isso mostra um certo grau de preferência, pois preferimos as conexões de primeiro grau, já que elas estão mais próximas (caminho mínimo). Se nenhuma delas for o que queremos, então passamos para o segundo grau, e assim por diante. Percebe-se que é necessário uma ordem ou uma fila para organizar essa ideia de preferência e grau.

A pesquisa em largura já faz isso e ela utiliza a **estrutura de dados fila**

### O que é Fila?

Fila é uma estrutura de dados que funciona exatamente como uma fila da vida real.

![[fila1.png]]

O funcionamento é igual a [[Pilha]]. Mas, a pessoa que foi add primeiro na fila é a primeira a ser retirada. 

- Fila é **FIFO (First in, First out)** - primeiro a entrar, primeiro a sair.
- Pilha é **LIFO(Last in, First out)** - último a entrar, primeiro a sair.

A fila tem duas funcionalidades push (enqueue) e pop (dequeue).

![[fila2.png]]

