# 🔗 Kruskal's Algorithm for Minimum Spanning Tree (MST)


## 🖼️ Visual Representation

![Kruskal's Algorithm Visualization](https://upload.wikimedia.org/wikipedia/commons/b/bb/Kruskal_Algorithm_Animation.gif)


## 🐍 Python Code
### Implementation:
```python
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal_algorithm(graph):
    vertices = set()
    for u, v, _ in graph:
        vertices.update([u, v])

    ds = DisjointSet(vertices)
    mst = []
    graph.sort(key=lambda edge: edge[2])  # Sort edges by weight

    for u, v, weight in graph:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, weight))
            ds.union(u, v)

    return mst

# Example usage:
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 6),
    ('C', 'D', 3)
]
mst = kruskal_algorithm(edges)

# Print MST
print("Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} - {v}, Weight: {weight}")
# Output:
# Minimum Spanning Tree:
# A - B, Weight: 1
# B - C, Weight: 2
# C - D, Weight: 3
````

## 🔑 Key Features

* **Type**: Greedy algorithm for Minimum Spanning Tree.
* **Works With**: Undirected, connected, and weighted graphs.
* **Time Complexity**: $O(E \cdot \log E + E \cdot \alpha(V))$, where:

  * $E$: Edges in the graph.
  * $V$: Vertices in the graph.
  * $\alpha(V)$: Inverse Ackermann function (from union-find).
* **Space Complexity**: $O(V + E)$, for the graph and disjoint set.

## ⚙️ Algorithm Steps

1. Sort all edges by weight.
2. Initialize disjoint sets for all vertices.
3. Iterate through the sorted edges:

   * Add the edge to the MST if it doesn’t form a cycle.
   * Union the sets of the two vertices.
4. Stop when the MST has $V - 1$ edges.

## 🛠️ Applications

* **Network Design**: Cost-effective electrical wiring and internet connections.
* **Clustering**: Hierarchical clustering in machine learning.
* **Transportation**: Planning low-cost road systems.
