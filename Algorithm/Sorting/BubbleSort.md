# 🫧 Bubble Sort Cheat Sheet

## 🐍 Python Code
### Standard Version:
```python
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
```

### Optimized Version:
```python
def bubble_sort_optimized(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
```

## 🔑 Key Features
- **Type**: Comparison-based sorting.
- **Time Complexity**:
  - 🟢 Best: \(O(n)\)
  - 🟡 Average: \(O(n^2)\)
  - 🔴 Worst: \(O(n^2)\)
- **Space Complexity**: \(O(1)\)

## ⚙️ Algorithm Steps
1. Compare adjacent elements.
2. Swap if out of order.
3. Repeat until sorted.
