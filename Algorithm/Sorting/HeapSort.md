# 🏔️ Heap Sort

## 🖼️ Visual Representation

![Heap Sort Steps](../../Resources/Heap_sort_example.gif)

## 🐍 Python Code
### Standard Version:
```python
def heapify(array, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child is larger than root
    if left < n and array[left] > array[largest]:
        largest = left

    # Check if right child is larger than largest so far
    if right < n and array[right] > array[largest]:
        largest = right

    # Swap and continue heapifying if root is not largest
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heap_sort(array):
    n = len(array)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # Swap
        heapify(array, i, 0)
````

## 🔑 Key Features

* **Type**: Comparison-based sorting.
* **Time Complexity**:

  * 🟢 Best: $O(n \log n)$
  * 🟡 Average: $O(n \log n)$
  * 🔴 Worst: $O(n \log n)$
* **Space Complexity**: $O(1)$ (in-place sorting).

## ⚙️ Algorithm Steps

1. **Build a Max Heap**: Rearrange the array into a binary heap.
2. **Extract Elements**: Swap the root (largest element) with the last item and reduce the heap size.
3. **Heapify**: Restore the heap property after each extraction.
