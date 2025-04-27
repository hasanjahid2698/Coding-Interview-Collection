# 🔀 Merge Sort

## 🖼️ Visual Representation
![Merge Sort Steps](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

## 🐍 Python Code
### Standard Version:
```python
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Recursive calls
        merge_sort(left)
        merge_sort(right)

        # Merging the sorted halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
```

## 🔑 Key Features
- **Type**: Divide-and-conquer sorting.
- **Time Complexity**:
  - 🟢 Best: \(O(n \log n)\)
  - 🟡 Average: \(O(n \log n)\)
  - 🔴 Worst: \(O(n \log n)\)
- **Space Complexity**: \(O(n)\) (due to auxiliary arrays).

## ⚙️ Algorithm Steps
1. **Divide**: Split the array into two halves until each half has one or zero elements.
2. **Conquer**: Recursively sort the two halves.
3. **Merge**: Combine the sorted halves into a single sorted array.
