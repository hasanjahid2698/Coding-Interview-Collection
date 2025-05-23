# 🔄 Topological Sort

## 🖼️ Visual Representation
![Topological Sort Visualization](../Resources/topological_sort.gif)

## 🐍 Python Code

### Using DFS:
```python
def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]

# Example Usage:
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}
print("Topological Sort (DFS):", topological_sort_dfs(graph))
# Output: ['B', 'A', 'D', 'C', 'E', 'H', 'F', 'G']
````

### Using BFS (Kahn's Algorithm):

```python
from collections import deque

def topological_sort_bfs(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque([node for node in graph if indegree[node] == 0])
    topo_order = []

    while queue:
        current = queue.popleft()
        topo_order.append(current)
        for neighbor in graph.get(current, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return topo_order

# Example Usage:
print("Topological Sort (BFS):", topological_sort_bfs(graph))
# Output: ['B', 'A', 'D', 'C', 'E', 'H', 'F', 'G']
```

## 🔑 Key Features

* **Type**: Graph algorithm for Directed Acyclic Graphs (DAGs).
* **Purpose**: Linear ordering of vertices such that for any directed edge $u \to v$, $u$ comes before $v$.
* **Time Complexity**:

  * **DFS**: $O(V + E)$
  * **BFS (Kahn's)**: $O(V + E)$
* **Space Complexity**: $O(V)$ for visited nodes or indegree tracking.

## ⚙️ Algorithm Steps

### **DFS-Based Approach**:

1. Traverse each unvisited node recursively.
2. Mark nodes visited and push them to a stack after exploring all neighbors.
3. Reverse the stack to get the topological order.

### **BFS (Kahn's Algorithm)**:

1. Compute in-degrees for all vertices.
2. Enqueue vertices with zero in-degree.
3. Process each vertex, reducing the in-degree of its neighbors.
4. Add neighbors with zero in-degree to the queue.

## 🛠️ Applications

* **Task Scheduling**: Determining the order of tasks with dependencies.
* **Course Prerequisites**: Ensuring prerequisites are completed first.
* **Build Systems**: Managing build order in software projects.

