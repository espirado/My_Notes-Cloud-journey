import heapq

class Graph:
    def __init__(self, directed=False):
        self.adj = {}  # node -> {neighbor: weight}
        self.directed = directed

    def add_edge(self, u, v, w):
        """Add an edge from u to v with weight w. If undirected, add both ways."""
        self.adj.setdefault(u, {})[v] = w
        if not self.directed:
            self.adj.setdefault(v, {})[u] = w

    def remove_edge(self, u, v):
        """Remove the edge from u to v. If undirected, remove both ways."""
        if v in self.adj.get(u, {}):
            del self.adj[u][v]
        if not self.directed and u in self.adj.get(v, {}):
            del self.adj[v][u]

    def update_edge(self, u, v, w):
        """Update the weight of the edge from u to v. If undirected, update both ways."""
        if v in self.adj.get(u, {}):
            self.adj[u][v] = w
        if not self.directed and u in self.adj.get(v, {}):
            self.adj[v][u] = w

# 1. Detect network partitions (connected components)
def connected_components(graph):
    visited = set()
    components = []
    for node in graph.adj:
        if node not in visited:
            stack = [node]
            comp = []
            while stack:
                n = stack.pop()
                if n not in visited:
                    visited.add(n)
                    comp.append(n)
                    stack.extend(graph.adj[n])
            components.append(comp)
    return components

# 2. Minimum Spanning Tree (Kruskal's algorithm)
def kruskal_mst(graph):
    parent = {}
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    def union(u, v):
        pu, pv = find(u), find(v)
        if pu != pv:
            parent[pu] = pv

    edges = []
    for u in graph.adj:
        for v, w in graph.adj[u].items():
            if graph.directed or u < v:  # avoid duplicates for undirected
                edges.append((w, u, v))
    edges.sort()
    for node in graph.adj:
        parent[node] = node
    mst = []
    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
    return mst

# 3. Shortest Path (Dijkstra's algorithm)
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph.adj}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph.adj[u].items():
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist

# Example usage for SRE/infra topology
def _example():
    print("--- Undirected Graph Example ---")
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'C', 2)
    g.add_edge('C', 'D', 1)
    g.add_edge('D', 'A', 4)
    g.add_edge('B', 'D', 3)
    g.add_edge('E', 'F', 1)  # Disconnected component
    g.add_edge('A', 'A', 0)  # Self-loop

    print("Connected components:", connected_components(g))
    print("MST:", kruskal_mst(g))
    print("Shortest paths from A:", dijkstra(g, 'A'))

    # Edge case: Remove non-existent edge
    g.remove_edge('X', 'Y')
    # Edge case: Update non-existent edge
    g.update_edge('X', 'Y', 5)
    # Dynamic edge update
    g.update_edge('A', 'B', 10)
    print("After updating edge A-B to weight 10:")
    print("Shortest paths from A:", dijkstra(g, 'A'))

    print("\n--- Directed Graph Example ---")
    dg = Graph(directed=True)
    dg.add_edge('A', 'B', 1)
    dg.add_edge('B', 'C', 2)
    dg.add_edge('C', 'D', 1)
    dg.add_edge('D', 'A', 4)
    dg.add_edge('B', 'D', 3)
    dg.add_edge('E', 'F', 1)
    dg.add_edge('A', 'A', 0)  # Self-loop

    print("Connected components:", connected_components(dg))
    print("MST (not meaningful for directed, but shown):", kruskal_mst(dg))
    print("Shortest paths from A:", dijkstra(dg, 'A'))

if __name__ == "__main__":
    _example() 