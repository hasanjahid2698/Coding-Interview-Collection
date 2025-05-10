# 🌐 Breadth-First Search (BFS)

## 🖼️ Visual Representation

![BFS Visualization](../../Resources/BFS.gif)

## 🐍 Python Code
### BFS for a Graph:
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])
    return result

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print(bfs(graph, 'A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']
````

## 🔑 Key Features

* **Type**: Graph traversal algorithm.
* **Works With**: Directed/Undirected Graphs, Trees.
* **Time Complexity**: $O(V + E)$, where $V$ is vertices and $E$ is edges.
* **Space Complexity**: $O(V)$ (for visited nodes and queue).

## ⚙️ Algorithm Steps

1. **Initialization**: Use a queue and a visited set.
2. **Start**: Enqueue the starting node.
3. **Traversal**:
   * Dequeue a node, mark it as visited.
   * Enqueue all unvisited neighbors.
4. **Repeat** until the queue is empty.

## 🛠️ Applications

* **Shortest Path**: In unweighted graphs.
* **Social Network Analysis**: Finding connections.
* **Web Crawlers**: Crawling web pages layer by layer.
* **Solving Mazes**: Exploring paths systematically.
