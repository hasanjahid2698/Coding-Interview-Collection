# 🌟 Pre-Order Traversal (DFS)


## 🖼️ Visual Representation

![Pre-Order Traversal](../../Resources/pre-order-traversal.gif)

## 🐍 Python Code
### Recursive Implementation:
```python
def pre_order_recursive(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.value)
        pre_order_recursive(node.left, result)
        pre_order_recursive(node.right, result)
    return result

# Example usage:
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Tree structure:
#       A
#      / \
#     B   C
#    / \
#   D   E
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')

print(pre_order_recursive(root))  # Output: ['A', 'B', 'D', 'E', 'C']
````


## 🔑 Key Features

* **Type**: Depth-First Traversal.
* **Order**: Root → Left → Right.
* **Time Complexity**: $O(n)$, where $n$ is the number of nodes.
* **Space Complexity**: $O(h)$, where $h$ is the height of the tree (recursive stack or explicit stack).

## ⚙️ Algorithm Steps

1. Visit the current node (root).
2. Traverse the left subtree recursively.
3. Traverse the right subtree recursively.

## 🛠️ Applications

* **Tree Copying**: Used to create a replica of the tree.
* **Expression Trees**: Recovers prefix expressions.
* **Directory Traversal**: Exploring a file structure.
