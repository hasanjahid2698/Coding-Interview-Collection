# 🛤️ Bellman-Ford Algorithm

## 🖼️ Visual Representation

https://github.com/user-attachments/assets/4c72c1dc-53b9-4a4c-82dd-1c3a6259d943

## 🐍 Python Code
### Implementation:
```python
def bellman_ford_with_path(graph, edges, start):
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}

    distances[start] = 0

    # Relax edges (V - 1) times
    for _ in range(len(graph) - 1):
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u

    # Check for negative-weight cycles
    for u, v, weight in edges:
        if distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return distances, predecessors

def reconstruct_path(predecessors, start, end):
    if predecessors[end] is None:
        return None  # No path exists
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    return path

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
distances, predecessors = bellman_ford_with_path(graph, edges, start_node)

# Print shortest distances
print("Shortest Distances:")
for node in distances:
    print(f"{node}: {distances[node]}")

# Print path from A to D
start, end = 'A', 'D'
path = reconstruct_path(predecessors, start, end)
print(f"Path from {start} to {end}: {path}")
# Output: Path from A to D: ['A', 'B', 'D']
````

## 🔑 Key Features

* **Type**: Single-source shortest path algorithm with path generation.
* **Works With**: Weighted graphs, including negative weights.
* **Time Complexity**: $O(V \cdot E)$, where $V$ is vertices and $E$ is edges.
* **Space Complexity**: $O(V)$, for distance and predecessor storage.

## ⚙️ Algorithm Steps

1. Initialize:

   * Set distances to $\infty$ for all nodes, except $\text{start} = 0$.
   * Set predecessors of all nodes to `None`.
2. Relax all edges $V - 1$ times:

   * Update distance and predecessor for each edge if a shorter path is found.
3. Check for negative-weight cycles:

   * If further relaxation is possible, a cycle exists.
4. Reconstruct the shortest path using predecessors.

## 🛠️ Applications

* **Currency Arbitrage**: Detecting negative cycles in exchange rates.
* **Shortest Paths**: Useful for graphs with negative edge weights.
* **Routing**: Network packet delivery with path visualization.

## ⚠️ Limitations

* Cannot handle graphs with negative-weight cycles.




