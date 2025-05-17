# 🛤️ Bellman-Ford Algorithm

## 🖼️ Visual Representation

![Bellman-Ford Algorithm Visualization](../../../Resources/Bellman_ford.mp4)


## 🐍 Python Code
### Implementation:
```python
def bellman_ford(graph, edges, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Check for negative-weight cycles
    for u, v, weight in edges:
        if distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return distances

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 6),
    ('C', 'D', 3)
]
start_node = 'A'
print(bellman_ford(graph, edges, start_node))
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 6}
````

## 🔑 Key Features

* **Type**: Single-source shortest path algorithm.
* **Works With**: Weighted graphs, including negative weights.
* **Time Complexity**: $O(V \cdot E)$, where $V$ is vertices and $E$ is edges.
* **Space Complexity**: $O(V)$, for distance storage.

## ⚙️ Algorithm Steps

1. Initialize distances to infinity ($\infty$) for all nodes except the start node ($0$).
2. Relax all edges $V - 1$ times:
   * Update the distance to each vertex if a shorter path is found.
3. Perform one additional iteration to check for negative-weight cycles.

## 🛠️ Applications
* **Currency Arbitrage**: Detecting negative cycles in currency exchange rates.
* **Shortest Paths**: Useful for graphs with negative edge weights.
* **Routing**: Network packet delivery in certain systems.

## ⚠️ Limitations
* Cannot work with graphs containing negative-weight cycles.

