from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node, name=None):
        self.nodes[node] = name if name else node
        self.edges[node] = []

    def add_edge(self, from_node, to_node, weight=1):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

    def neighbors(self, node):
        return self.edges.get(node, [])


def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]

    while queue:
        (node, path) = queue.pop(0)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.neighbors(node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None


def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]

    while stack:
        (node, path) = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.neighbors(node):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None


def heuristic(a, b):
    return 1


def a_star_search(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start]))
    visited = set()

    while not pq.empty():
        (cost, node, path) = pq.get()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.neighbors(node):
                if neighbor not in visited:
                    priority = cost + weight + heuristic(neighbor, goal)
                    pq.put((priority, neighbor, path + [neighbor]))
    return None
