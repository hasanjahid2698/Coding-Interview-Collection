# 🪜 Insertion Sort

## 🐍 Python Code
### Standard Version:
```python
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
```

## 🔑 Key Features
- **Type**: Comparison-based sorting.
- **Time Complexity**:
  - 🟢 Best: \(O(n)\)
  - 🟡 Average: \(O(n^2)\)
  - 🔴 Worst: \(O(n^2)\)
- **Space Complexity**: \(O(1)\)

## ⚙️ Algorithm Steps
1. Start from the second element.
2. Pick the current element and compare it with elements before it.
3. Shift larger elements one position to the right.
4. Insert the current element into its correct position.
5. Repeat for all elements.

## 🖼️ Visual Representation
![Insertion Sort Steps](https://upload.wikimedia.org/wikipedia/commons/4/42/Insertion_sort.gif)
```

This Markdown includes an image hosted on Wikipedia that visually explains Insertion Sort. If you need a custom image or specific illustration, let me know!
