# 🚦 Dijkstra's Algorithm

## 🖼️ Visual Representation

![Dijkstra's Algorithm Visualization](../../../Resources/Dijkstra.gif)

## 🐍 Python Code
### Implementation:
```python
import heapq

def dijkstra_with_path(graph, start):
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip nodes already processed with a shorter distance
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

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
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3},
    'D': {}
}
start_node = 'A'
distances, predecessors = dijkstra_with_path(graph, start_node)

# Print shortest distances
print("Shortest Distances:")
for node in distances:
    print(f"{node}: {distances[node]}")

# Print path from A to D
start, end = 'A', 'D'
path = reconstruct_path(predecessors, start, end)
print(f"Path from {start} to {end}: {path}")
# Output: Path from A to D: ['A', 'B', 'C', 'D']
````

## 🔑 Key Features

* **Type**: Single-source shortest path algorithm with path generation.
* **Works With**: Weighted graphs with non-negative weights.
* **Time Complexity**: $O((V + E) \cdot \log V)$, where $V$ is vertices and $E$ is edges.
* **Space Complexity**: $O(V + E)$, for the graph, distances, and priority queue.

## ⚙️ Algorithm Steps

1. Initialize:

   * Set all distances to $\infty$, except $\text{start} = 0$.
   * Use a priority queue to process nodes.
2. Extract the minimum distance node from the queue.
3. Update the distance and predecessor for each neighbor if a shorter path is found.
4. Continue until all nodes are processed.
5. Reconstruct the shortest path using the predecessors.

## 🛠️ Applications

* **Routing and Navigation**: Shortest path in road networks.
* **Network Optimization**: Optimal packet routing in networks.
* **Game Development**: AI pathfinding (e.g., A\* builds on Dijkstra).

## ⚠️ Limitations

* Cannot handle graphs with negative-weight edges.

