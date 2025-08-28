import os
import pandas as pd
import clustering
from graph_utils import Graph, a_star_search, bfs, dfs

DATA_DIR = "data"
NODES_FILE = os.path.join(DATA_DIR, "nodes.csv")
EDGES_FILE = os.path.join(DATA_DIR, "edges.csv")

def main():
    print("Executando clustering...")
    clustering.main()
    print("Carregando grafo...")
    graph = Graph()
    nodes_df = pd.read_csv(NODES_FILE)
    edges_df = pd.read_csv(EDGES_FILE)
    for _, row in nodes_df.iterrows():
        graph.add_node(row["id"], row["name"])
    for _, row in edges_df.iterrows():
        graph.add_edge(row["from"], row["to"], row["weight"])
    start, goal = "A", "C"
    print("\nResultados das buscas:")
    print("BFS:", bfs(graph, start, goal))
    print("DFS:", dfs(graph, start, goal))
    print("A*:", a_star_search(graph, start, goal))

if __name__ == "__main__":
    main()