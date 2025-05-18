# 🌳 Disjoint Set Union-Find Data Structure

## 🖼️ Visual Representation

![Disjoint Set Visualization](https://upload.wikimedia.org/wikipedia/commons/d/d1/Disjoint-set.svg)


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

# Example usage:
vertices = ['A', 'B', 'C', 'D', 'E']
ds = DisjointSet(vertices)

# Perform unions
ds.union('A', 'B')
ds.union('B', 'C')

# Find representatives
print(ds.find('A'))  # Output: Representative of 'A'
print(ds.find('C'))  # Output: Representative of 'C'

# Check if two elements are in the same set
print(ds.find('A') == ds.find('C'))  # Output: True
print(ds.find('A') == ds.find('D'))  # Output: False
````

## 🔑 Key Features

* **Type**: Data structure for maintaining partitioned sets.
* **Operations**:

  * **Find**: Determines the representative of the set containing an element.
  * **Union**: Combines two sets into one.
* **Optimizations**:

  * **Path Compression**: Makes the tree flatter, speeding up subsequent operations.
  * **Union by Rank**: Balances the tree by attaching smaller trees under larger ones.

## ⚙️ Algorithm Steps

1. **Initialization**:

   * Each element starts in its own set.
   * The parent of each element is itself.
2. **Find**:

   * Traverse up the tree to find the root of the set.
   * Use path compression to make future lookups faster.
3. **Union**:

   * Use the `find` operation to determine the roots of the sets.
   * Attach the smaller tree under the larger tree (union by rank).

## 🛠️ Applications

* **Kruskal's Algorithm**: For Minimum Spanning Tree construction.
* **Dynamic Connectivity**: Checking if two elements are in the same connected component.
* **Clustering**: Grouping data into clusters in machine learning.

## 📈 Time Complexity

* **Find**: $O(\alpha(V))$, where $\alpha$ is the inverse Ackermann function.
* **Union**: $O(\alpha(V))$.
* **Space Complexity**: $O(V)$.
