
# ⚡ Quick Sort

## 🖼️ Visual Representation

![Quick Sort Steps](../../Resources/quicksort.gif)


## 🐍 Python Code
### Standard Version:
```python
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[len(array) // 2]
        left = [x for x in array if x < pivot]
        middle = [x for x in array if x == pivot]
        right = [x for x in array if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
````

### In-Place Version:

```python
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort_inplace(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort_inplace(array, low, pi - 1)
        quick_sort_inplace(array, pi + 1, high)
```

## 🔑 Key Features

* **Type**: Divide-and-conquer sorting.
* **Time Complexity**:

  * 🟢 Best: $O(n \log n)$
  * 🟡 Average: $O(n \log n)$
  * 🔴 Worst: $O(n^2)$ (when pivot selection is poor).
* **Space Complexity**:

  * $O(\log n)$ for recursive stack (in-place version).

## ⚙️ Algorithm Steps

1. **Choose a Pivot**: Select an element as a pivot.
2. **Partition**: Rearrange the array so elements smaller than the pivot are on the left and larger ones are on the right.
3. **Recursion**: Recursively apply the steps to the sub-arrays.

