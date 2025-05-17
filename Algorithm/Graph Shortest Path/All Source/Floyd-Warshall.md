# 🌐 Floyd-Warshall Algorithm with Path Reconstruction

## 🖼️ Visual Representation
https://github.com/user-attachments/assets/ffdf93b0-35af-40db-9913-82b82aff9d6e

## 🐍 Python Code
### Implementation:
```python
def floyd_warshall_with_path(graph):
    nodes = list(graph.keys())
    n = len(nodes)

    # Initialize distance and next matrices
    distance = {u: {v: float('inf') for v in nodes} for u in nodes}
    next_node = {u: {v: None for v in nodes} for u in nodes}

    for u in nodes:
        distance[u][u] = 0  # Distance to itself is 0
        for v, weight in graph[u].items():
            distance[u][v] = weight
            next_node[u][v] = v  # Next step on the path

    # Update distances and paths
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    next_node[i][j] = next_node[i][k]

    return distance, next_node

def reconstruct_path(next_node, start, end):
    if next_node[start][end] is None:
        return None  # No path exists
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    return path

# Example usage:
graph = {
    'A': {'B': 3, 'C': 8, 'D': -4},
    'B': {'D': 1, 'A': 3},
    'C': {'B': 4},
    'D': {'C': 7, 'A': -4}
}
distances, next_node = floyd_warshall_with_path(graph)

# Print shortest distances
print("Shortest Distances:")
for u in distances:
    print(f"{u}: {distances[u]}")

# Print path from A to C
start, end = 'A', 'C'
path = reconstruct_path(next_node, start, end)
print(f"Path from {start} to {end}: {path}")
# Output: Path from A to C: ['A', 'D', 'C']
````

## 🔑 Key Features

* **Type**: All-pairs shortest path algorithm with path generation.
* **Works With**: Weighted graphs (including negative weights, but no negative cycles).
* **Time Complexity**: $O(V^3)$, where $V$ is the number of vertices.
* **Space Complexity**: $O(V^2)$, for the distance and next matrices.

## ⚙️ Algorithm Steps

1. Create a distance matrix initialized with edge weights and a next matrix for path reconstruction.
2. For each intermediate node $k$:

   * Update the distance and next matrices for all pairs $i, j$:

     $$
     \text{distance}[i][j] = \min(\text{distance}[i][j], \text{distance}[i][k] + \text{distance}[k][j])
     $$

     Update the next node for $i$ to $j$ through $k$.
3. Reconstruct paths using the next matrix.

## 🛠️ Applications

* **Shortest Paths**: Solves all-pairs shortest path problems with explicit path generation.
* **Network Analysis**: Routing with path visualization.
* **Transitive Closure**: Finding reachability and specific paths.

## ⚠️ Limitations

* Does not handle graphs with negative-weight cycles.
