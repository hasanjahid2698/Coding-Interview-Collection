
# 🌲 Prim's Algorithm for Minimum Spanning Tree (MST)

## 🖼️ Visual Representation

![Prim's Algorithm Visualization](../Resources/Prim-animation.gif)

## 🐍 Python Code
### Implementation:
```python
import heapq

def prims_algorithm(graph, start):
    mst = []  # List to store MST edges
    visited = set()  # Track visited nodes
    priority_queue = [(0, start, None)]  # (weight, current_node, parent)

    while priority_queue:
        weight, current_node, parent = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)
        if parent is not None:
            mst.append((parent, current_node, weight))

        for neighbor, edge_weight in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(priority_queue, (edge_weight, neighbor, current_node))

    return mst

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}
start_node = 'A'
mst = prims_algorithm(graph, start_node)

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
* **Time Complexity**: $O((V + E) \cdot \log V)$, where $V$ is vertices and $E$ is edges.
* **Space Complexity**: $O(V + E)$, for the graph and priority queue.

## ⚙️ Algorithm Steps

1. Start with an arbitrary node and initialize a priority queue.
2. Pick the edge with the smallest weight that connects a visited node to an unvisited node.
3. Add the edge to the MST and mark the node as visited.
4. Repeat until all nodes are visited.

## 🛠️ Applications

* **Network Design**: Optimal wiring and pipeline layouts.
* **Telecommunications**: Designing efficient networks.
* **Transportation**: Building cost-effective road or railway systems.


