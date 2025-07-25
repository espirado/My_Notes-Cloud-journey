import concurrent.futures
from collections import defaultdict

class ParallelGraph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # undirected

    def pagerank(self, num_iter=10, damping=0.85):
        nodes = list(self.adj)
        N = len(nodes)
        rank = {n: 1.0 / N for n in nodes}
        for _ in range(num_iter):
            new_rank = {}
            def compute_rank(n):
                s = sum(rank[nb] / len(self.adj[nb]) for nb in self.adj[n])
                return n, (1 - damping) / N + damping * s
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for n, r in executor.map(compute_rank, nodes):
                    new_rank[n] = r
            rank = new_rank
        return rank

    def connected_components(self):
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
        for n in self.adj:
            parent[n] = n
        with concurrent.futures.ThreadPoolExecutor() as executor:
            list(executor.map(lambda e: union(e[0], e[1]), [(u, v) for u in self.adj for v in self.adj[u]]))
        comps = defaultdict(list)
        for n in self.adj:
            comps[find(n)].append(n)
        return list(comps.values())

    def parallel_bfs(self, start):
        from queue import Queue
        visited = set([start])
        q = Queue()
        q.put(start)
        while not q.empty():
            u = q.get()
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for v in self.adj[u]:
                    if v not in visited:
                        visited.add(v)
                        q.put(v)
        return visited

# Example usage
if __name__ == "__main__":
    g = ParallelGraph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    g.add_edge('E', 'F')
    print("PageRank:", g.pagerank())
    print("Connected Components:", g.connected_components())
    print("Parallel BFS from A:", g.parallel_bfs('A')) 