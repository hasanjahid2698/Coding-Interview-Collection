# 🔍 Selection Sort


## 🖼️ Visual Representation
![Selection Sort Steps](../../Resources/Selection.gif)

## 🐍 Python Code
### Standard Version:
```python
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
```

## 🔑 Key Features
- **Type**: Comparison-based sorting.
- **Time Complexity**:
  - 🟢 Best: \(O(n^2)\)
  - 🟡 Average: \(O(n^2)\)
  - 🔴 Worst: \(O(n^2)\)
- **Space Complexity**: \(O(1)\)

## ⚙️ Algorithm Steps
1. Divide the array into a sorted and unsorted part.
2. Find the minimum element in the unsorted part.
3. Swap it with the first element of the unsorted part.
4. Expand the sorted part by one element.
5. Repeat until the entire array is sorted.
