# 🚦 Dijkstra's Algorithm

## 🖼️ Visual Representation

![Dijkstra's Algorithm Visualization](../../../Resources/Dijkstra.gif)


## 🐍 Python Code
### Implementation:
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, node)
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}
start_node = 'A'
print(dijkstra(graph, start_node))
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 6}
````

## 🔑 Key Features

* **Type**: Single-source shortest path algorithm.
* **Works With**: Weighted graphs (non-negative weights only).
* **Time Complexity**: $O((V + E) \log V)$, where $V$ is vertices and $E$ is edges.
* **Space Complexity**: $O(V)$, for distances and priority queue.

## ⚙️ Algorithm Steps

1. Initialize distances to infinity ($\infty$) for all nodes except the start node ($0$).
2. Use a priority queue (min-heap) to select the node with the smallest distance.
3. Update the distances to all unvisited neighbors of the current node.
4. Mark the current node as visited and repeat until all nodes are processed.

## 🛠️ Applications

* **Network Routing**: Finding shortest paths in computer networks.
* **Map Navigation**: GPS applications for shortest routes.
* **Resource Optimization**: Transport, logistics, and flow analysis.
