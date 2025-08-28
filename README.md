
# ROTA INTELIGENTE: Otimização de Entregas com Algorítimos de IA

A Sabor Express é uma empresa local de delivery de alimentos que atua na região central da cidade. Apesar do crescimento na demanda por entregas, especialmente nos horários de pico, a empresa enfrenta dificuldades em manter a eficiência logística, resultando em atrasos, aumento de custos operacionais e insatisfação dos clientes. Atualmente, a definição das rotas de entrega é realizada de forma manual, baseando-se apenas na experiência dos entregadores, sem apoio de ferramentas tecnológicas que auxiliem na tomada de decisão. Nesse contexto, o uso de técnicas de Inteligência Artificial surge como uma alternativa estratégica para otimizar o processo de entregas. A modelagem da malha urbana por meio de grafos permite representar pontos de entrega como vértices e ruas como arestas, com pesos relacionados a distâncias ou tempos de deslocamento. A partir dessa estrutura, torna-se viável implementar algoritmos de busca, como A*, BFS e DFS, para identificar rotas mais curtas e eficientes.

Esse projeto tem como objetivo propor uma solução computacional baseada em Inteligência Artificial para otimização de rotas de entrega, explorando conceitos de grafos, algoritmos de busca e aprendizado não supervisionado. A solução será implementada em linguagem Python, com documentação detalhada e análise dos resultados obtidos.


## Contextualização do problema e objetivos

A Sabor Express, empresa responsável por entregas de alimentos na região central da cidade, enfrenta dificuldades logísticas que comprometem a qualidade do serviço prestado. Durante os períodos de maior movimento, como o horário de almoço e o jantar, os entregadores percorrem trajetos ineficientes, definidos manualmente, sem suporte de ferramentas tecnológicas que auxiliem na escolha das melhores rotas. Essa prática tem resultado em atrasos, aumento no consumo de combustível e redução da satisfação dos clientes.

Diante desse cenário, o desafio central consiste em desenvolver uma solução inteligente, baseada em algoritmos de Inteligência Artificial, que permita otimizar as entregas. O projeto propõe representar a malha viária da cidade como um grafo, em que os vértices correspondem a bairros ou pontos de entrega, enquanto as arestas representam as ruas, com pesos definidos a partir da distância ou do tempo estimado de deslocamento. A partir dessa modelagem, serão aplicados algoritmos de busca clássicos, como A*, BFS e DFS, para identificar trajetos mais curtos e eficientes.

Além disso, será empregada uma abordagem de aprendizado não supervisionado para o agrupamento de entregas. Por meio do algoritmo K-Means, pedidos próximos serão organizados em zonas de atendimento, reduzindo o esforço operacional e permitindo que cada entregador atenda a uma área específica. Essa estratégia visa melhorar o planejamento logístico, minimizar o tempo de deslocamento e ampliar a capacidade de atendimento.

Com isso, podemos definir os objetivos desse trabalho em uma lista simplificada para fácil entendimento:
- Desenvolver uma solução computacional que modele o sistema de entregas como um grafo, permitindo simulações e análises.
- Implementar algoritmos de busca para a identificação de rotas otimizadas.
- Aplicar técnicas de aprendizado não supervisionado para o agrupamento de pontos de entrega.
- Avaliar a eficiência da solução com base em métricas de desempenho, identificando ganhos em tempo e custo operacional.
- Fornecer uma documentação completa que descreva o processo de desenvolvimento, os resultados obtidos e as oportunidades de melhoria.
## Abordagem Adotada

A solução proposta para o problema da Sabor Express será desenvolvida em etapas, com o objetivo de garantir clareza, eficiência e possibilidade de expansão futura. Inicialmente, a cidade será modelada como um grafo ponderado, representando pontos de entrega como vértices e ruas como arestas, com pesos atribuídos a partir da distância geográfica ou do tempo estimado de deslocamento. Essa modelagem permitirá a aplicação de algoritmos clássicos de busca para encontrar rotas mais curtas e viáveis.

O algoritmo A* será utilizado como principal ferramenta de cálculo de rotas por sua eficiência na exploração de grafos, sendo complementado por BFS (Busca em Largura) e DFS (Busca em Profundidade) para fins de comparação de desempenho. Em cenários de alta demanda, será implementado o algoritmo K-Means para realizar agrupamentos de pontos de entrega próximos, criando zonas de atendimento e facilitando a distribuição de pedidos entre entregadores.

A implementação será realizada em linguagem Python, utilizando bibliotecas como NetworkX para manipulação de grafos, Scikit-learn para algoritmos de clustering e Matplotlib para visualização dos resultados. O código será estruturado em módulos, com arquivos separados para o carregamento de dados, algoritmos de busca, algoritmos de agrupamento e geração de relatórios.

Além disso, serão definidos indicadores de desempenho para análise dos resultados, como número de nós explorados, tempo de execução dos algoritmos e distância total percorrida. Os resultados obtidos serão documentados, discutidos criticamente e apresentados por meio de gráficos e diagramas que evidenciem as melhorias alcançadas com a aplicação da solução.

### Grafos e Modelagem de Redes

Um grafo é uma estrutura matemática formada por um conjunto de vértices e arestas que os conectam. Formalmente, um grafo G é definido como `G = (V, E)`, em que V representa o conjunto de vértices e E representa o conjunto de arestas. Os grafos podem ser direcionados ou não direcionados, ponderados ou não ponderados, a depender da natureza das conexões e das informações associadas.

Na modelagem de sistemas logísticos, os grafos são amplamente utilizados para representar redes de transporte, em que cada vértice corresponde a um ponto geográfico, como bairros ou estabelecimentos, enquanto as arestas representam as rotas possíveis entre esses pontos. Quando essas arestas recebem valores associados, como distância ou tempo de deslocamento, o grafo passa a ser classificado como ponderado. Essa abordagem permite simular e analisar trajetos com maior precisão, possibilitando a aplicação de algoritmos para otimização de percursos.
## Contextualização do problema e objetivos

A Sabor Express, empresa responsável por entregas de alimentos na região central da cidade, enfrenta dificuldades logísticas que comprometem a qualidade do serviço prestado. Durante os períodos de maior movimento, como o horário de almoço e o jantar, os entregadores percorrem trajetos ineficientes, definidos manualmente, sem suporte de ferramentas tecnológicas que auxiliem na escolha das melhores rotas. Essa prática tem resultado em atrasos, aumento no consumo de combustível e redução da satisfação dos clientes.

Diante desse cenário, o desafio central consiste em desenvolver uma solução inteligente, baseada em algoritmos de Inteligência Artificial, que permita otimizar as entregas. O projeto propõe representar a malha viária da cidade como um grafo, em que os vértices correspondem a bairros ou pontos de entrega, enquanto as arestas representam as ruas, com pesos definidos a partir da distância ou do tempo estimado de deslocamento. A partir dessa modelagem, serão aplicados algoritmos de busca clássicos, como A*, BFS e DFS, para identificar trajetos mais curtos e eficientes.

Além disso, será empregada uma abordagem de aprendizado não supervisionado para o agrupamento de entregas. Por meio do algoritmo K-Means, pedidos próximos serão organizados em zonas de atendimento, reduzindo o esforço operacional e permitindo que cada entregador atenda a uma área específica. Essa estratégia visa melhorar o planejamento logístico, minimizar o tempo de deslocamento e ampliar a capacidade de atendimento.

Com isso, podemos definir os objetivos desse trabalho em uma lista simplificada para fácil entendimento:
- Desenvolver uma solução computacional que modele o sistema de entregas como um grafo, permitindo simulações e análises.
- Implementar algoritmos de busca para a identificação de rotas otimizadas.
- Aplicar técnicas de aprendizado não supervisionado para o agrupamento de pontos de entrega.
- Avaliar a eficiência da solução com base em métricas de desempenho, identificando ganhos em tempo e custo operacional.
- Fornecer uma documentação completa que descreva o processo de desenvolvimento, os resultados obtidos e as oportunidades de melhoria.
## Algoritmos Utilizados

Para a resolução do desafio proposto, foram aplicados algoritmos clássicos de inteligência artificial, cada um com funções específicas no contexto da otimização das entregas da Sabor Express.

1. ***K-Means***
O K-Means é um algoritmo de aprendizado não supervisionado utilizado para agrupar entregas próximas em clusters, de modo a otimizar o deslocamento dos entregadores. Cada cluster representa uma zona geográfica de entregas. No código, essa etapa está implementada no módulo `clustering.py`

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=k)
labels = kmeans.fit_predict(deliveries[['x', 'y']])
deliveries['cluster'] = labels
```
**Entradas**: coordenadas X e Y das entregas (deliveries.csv).
**Saídas**: cada entrega recebe um identificador de cluster (cluster) e os centros de cluster (cluster_center_x, cluster_center_y).
**Objetivo**: reduzir o tempo de deslocamento e agrupar entregas próximas para facilitar o planejamento das rotas.

2. ***Busca em Largura (BFS)***
A Busca em Largura (Breadth-First Search) é utilizada para explorar grafos de maneira sistemática, visitando os nós mais próximos antes de avançar. No contexto do projeto, permite simular rotas entre pontos do grafo.

```python
def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.neighbors(node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
```

**Objetivo**: encontrar caminhos entre nós de forma eficiente, útil para simular rotas possíveis entre entregas.

3. ***Busca em Profundidade (DFS)***
A Busca em Profundidade (Depth-First Search) explora os grafos priorizando profundidade, percorrendo um caminho completo antes de retroceder. Foi implementada também em graph_utils.py:

```python
def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.neighbors(node):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
```
**Objetivo**: fornece uma alternativa de busca para comparar rotas e verificar eficiência de diferentes métodos de exploração.

4. ***A* (A-Star)**
O A-Star (A)* é um algoritmo de busca informada que combina custo acumulado e uma heurística para encontrar o caminho mais curto. No projeto, permite simular rotas mais eficientes entre entregas:
```python
def a_star_search(graph, start, goal):
    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((0, start, [start]))
    visited = set()
    while not pq.empty():
        cost, node, path = pq.get()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.neighbors(node):
                if neighbor not in visited:
                    priority = cost + weight + heuristic(neighbor, goal)
                    pq.put((priority, neighbor, path + [neighbor]))
```

Objetivo: otimizar rotas considerando custos das ruas e fornecer caminhos mais rápidos para os entregadores.


## Diagrama de Solução

```lua
+------------------+       +----------------+       +-------------------+
|  deliveries.csv  |       |   nodes.csv    |       |     edges.csv     |
+------------------+       +----------------+       +-------------------+
          |                        |                       |
          |                        |                       |
          v                        v                       v
      +-----------------------------------------------------------+
      |                       clustering.py                       |
      |-----------------------------------------------------------|
      | - Leitura das entregas                                    |
      | - Aplicação do K-Means para agrupar entregas próximas     |
      | - Geração de CSV deliveries_clustered.csv                 |
      | - Geração de gráfico de clusters (clusters.png)           |
      +-----------------------------------------------------------+
                                    |
                                    v
      +-----------------------------------------------------------+
      |                       main.py                             |
      |-----------------------------------------------------------|
      | - Carrega grafo (nodes + edges)                           |
      | - Executa algoritmos de busca (BFS, DFS, A*)              |
      | - Integra clusters às rotas (opcional)                    |
      +-----------------------------------------------------------+
                                    |
                                    v
                    +-------------------------------+
                    | Resultados e análises finais  |
                    | - deliveries_clustered.csv    |
                    | - clusters.png                |
                    | - Rotas entre entregas        |
                    +-------------------------------+
```

### Explicação do Fluxo

1. **Entrada de dados**:
- deliveries.csv contém a lista de entregas com coordenadas X e Y.
- nodes.csv e edges.csv representam a cidade como um grafo, incluindo nós (bairros ou locais) e arestas (ruas com peso baseado em distância ou tempo estimado).

2. **Clustering (clustering.py)**:
- O algoritmo K-Means agrupa entregas próximas, reduzindo a complexidade da definição de rotas e aumentando a eficiência do serviço.
- Saídas: CSV com clusters e gráfico visualizando os grupos.

3. **Execução de buscas (main.py e graph_utils.py)**:
- O grafo da cidade é carregado, e os algoritmos BFS, DFS e A* são aplicados para encontrar rotas entre nós do grafo.
- Os clusters podem ser integrados posteriormente para definir rotas prioritárias para cada entregador.

4. **Resultados**:
- Arquivo CSV atualizado com clusters.
- Gráfico de clusters mostrando visualmente a distribuição das entregas.
## Discussão do Resultados

Após a implementação dos algoritmos de clustering e busca de rotas, o sistema foi testado com os dados simulados da Sabor Express, concluindo que:

1. ***Clustering das Entregas***

O algoritmo K-Means foi aplicado sobre as coordenadas das entregas, gerando agrupamentos que representam zonas geográficas próximas. O arquivo deliveries_clustered.csv contém os seguintes campos:

- id → identificador da entrega;
- x, y → coordenadas da entrega;
- cluster → identificador do cluster ao qual a entrega pertence;
- cluster_center_x, cluster_center_y → coordenadas do centro do cluster.

O gráfico clusters.png mostrou claramente que as entregas foram distribuídas em grupos compactos, facilitando a organização de rotas para cada entregador. A visualização confirma que o algoritmo conseguiu agrupar de forma coerente entregas próximas, atendendo ao objetivo de reduzir deslocamentos.

2. ***Algoritmos de Busca no Grafo***

Foram testados BFS, DFS e A* no grafo representando a cidade. Exemplos de caminhos encontrados entre nós do grafo demonstram:

- BFS: encontra rotas curtas em termos de número de nós percorridos, mas não necessariamente o menor custo.
- DFS: percorre caminhos profundos, podendo gerar trajetos mais longos, útil para explorar alternativas.
- A*: combina custo acumulado e heurística, resultando em rotas mais eficientes em termos de distância ou tempo.

A integração dos clusters com as rotas permite que cada entregador se concentre em uma zona específica, reduzindo a complexidade do planejamento e o tempo de deslocamento total.

3. ***Eficiência e Limitações***

Eficiência:
- O uso de K-Means reduziu a dispersão das entregas e facilitou a definição de zonas de entrega.
- A aplicação de A* no grafo proporciona caminhos próximos ao mínimo custo estimado, simulando entregas mais rápidas.

Limitações:

- O modelo assume que todas as ruas possuem pesos fixos, não considerando trânsito ou condições temporais.
- O clustering depende do número de clusters definido (k), que pode influenciar a eficiência das rotas.
- Para grandes volumes de entregas, a performance dos algoritmos de busca pode exigir otimizações adicionais.

4. Sugestões de Melhoria

- Incorporar dados em tempo real sobre trânsito para ajustes dinâmicos nas rotas.
- Automatizar a escolha do número ideal de clusters usando métodos como o cotovelo ou silhouette.
- Integrar o sistema a dispositivos móveis dos entregadores para fornecer rotas otimizadas em tempo real.
- Avaliar a implementação de algoritmos de roteamento mais avançados, como Dijkstra ou Veículos de Roteamento (VRP), para cenários com múltiplos entregadores.
## Considerações finais

O presente trabalho demonstrou a aplicação de técnicas de Inteligência Artificial para otimizar o processo de entregas da empresa fictícia Sabor Express. Por meio da implementação de K-Means, foi possível agrupar entregas próximas em clusters, o que facilita o planejamento de rotas e reduz deslocamentos desnecessários.

A utilização de algoritmos de busca clássicos, como BFS, DFS e A*, permitiu explorar o grafo que representa a cidade e encontrar caminhos eficientes entre os nós, simulando rotas que poderiam ser utilizadas pelos entregadores. Em particular, o algoritmo A* mostrou-se eficaz na identificação de rotas de menor custo estimado, considerando as distâncias entre os pontos do grafo. Os resultados obtidos indicam que a combinação de clustering e busca em grafos é uma estratégia viável para problemas logísticos de pequeno a médio porte. Além disso, a implementação prática do projeto, incluindo geração de arquivos CSV e gráficos de clusters, fornece ferramentas concretas para análise e suporte à tomada de decisão.

Apesar das limitações identificadas, como a ausência de dados dinâmicos de trânsito e a dependência do número de clusters definido, a solução apresentada cumpre os objetivos propostos. Sugere-se que trabalhos futuros considerem a integração de dados em tempo real, otimização de parâmetros de clustering e utilização de algoritmos avançados de roteamento, como Dijkstra ou VRP (Vehicle Routing Problem), para cenários mais complexos e de maior escala.

Portanto, a solução desenvolvida demonstra a eficácia de técnicas clássicas de IA na otimização de processos logísticos, oferecendo uma base sólida para melhorias futuras e aplicação prática em empresas de delivery que busquem maior eficiência operacional e satisfação dos clientes.