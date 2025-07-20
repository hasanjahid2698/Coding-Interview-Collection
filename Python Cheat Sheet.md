# Python Cheat Sheet

## Variables
```python
x = 5           # Integer
pi = 3.14       # Float
name = "Jahid"  # String
is_active = True # Boolean
```

## If Statements
```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# One-liner if
print("Positive") if x > 0 else print("Non-positive")
```

## Loops
### For Loop
```python
for i in range(5):
    print(i)

for x in range(2, 6):  # 2 to 6 (but not including 6)
  print(x)

for x in range(2, 30, 3): # Increment with 3 (default is 1)
  print(x)

for i, n in enumerate(nums):
  print(i, n)

```
### While Loop
```python
while x > 0:
    print(x)
    x -= 1
```

## Math
```python
import math

sqrt = math.sqrt(16)    # 4.0
power = pow(2, 3)       # 8
factorial = math.factorial(5)  # 120
```

## Arrays (Lists)
```python
arr = [1, 2, 3, 4, 5]
arr.append(6)          # [1, 2, 3, 4, 5, 6]
arr.pop()              # [1, 2, 3, 4, 5]
arr.insert(2, 99)      # [1, 2, 99, 3, 4, 5]
arr.remove(99)         # [1, 2, 3, 4, 5]
```

## Sorting
```python
nums = [3, 1, 4, 1, 5]
sorted_nums = sorted(nums)      # [1, 1, 3, 4, 5]
nums.sort(reverse=True)         # [5, 4, 3, 1, 1]
```

## List Comprehension
```python
squares = [x**2 for x in range(5)]     # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
```

## 2D Arrays
```python
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for col in row:
        print(col)

# Accessing elements
matrix[0][1] = 99  # Change 2 to 99
```

## Declaring 1D and 2D Arrays
```python
N = 5
arr1 = [0 for i in range(N)]

# 2d array
rows, cols = (5, 5)
arr2 = [[0 for i in range(cols)] for j in range(rows)]

```

## Strings
```python
s = "hello"
reversed_s = s[::-1]        # "olleh"
split_s = s.split("l")     # ['he', '', 'o']
joined_s = "-".join(["a", "b"])  # "a-b"
upper_s = s.upper()         # "HELLO"
lower_s = s.lower()         # "hello"
```

## Queues
```python
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)          # deque([1, 2, 3, 4])
queue.popleft()          # deque([2, 3, 4])
queue.appendleft(0)      # deque([0, 2, 3, 4])
queue.pop()              # deque([0, 2, 3])
queue.clear()            # deque([])
```

## Stack
```python
stack = []
stack.append(1)          # [1]
stack.append(2)          # [1, 2]
stack.pop()              # [1]
stack.extend([3, 4])     # [1, 3, 4]
stack[-1]                # Peek: 4
```

## Hash Sets
```python
unique = {1, 2, 3}
unique.add(4)            # {1, 2, 3, 4}
unique.remove(1)         # {2, 3, 4}
unique.discard(99)       # Safe removal
unique.clear()           # Set becomes empty
union = unique.union({5, 6})    # {2, 3, 4, 5, 6}
intersection = unique.intersection({3, 4, 7}) # {3, 4}
```

## Hash Maps
```python
map = {"a": 1, "b": 2}
map["c"] = 3             # {"a": 1, "b": 2, "c": 3}
del map["a"]             # {"b": 2, "c": 3}
keys = map.keys()         # dict_keys(["b", "c"])
values = map.values()     # dict_values([2, 3])
items = map.items()       # dict_items([("b", 2), ("c", 3)])
```

## Tuples
```python
t = (1, 2, 3)
print(t[0])              # 1
x, y, z = t              # x=1, y=2, z=3
new_t = t + (4, 5)       # (1, 2, 3, 4, 5)
```

## Heaps
```python
import heapq
nums = [3, 2, 1]
heapq.heapify(nums)       # Min-heap [1, 2, 3]
heapq.heappush(nums, 0)   # [0, 2, 1, 3]
heapq.heappop(nums)       # 0
heapq.nlargest(2, nums)   # [3, 2]
heapq.nsmallest(2, nums)  # [1, 2]
```

## Functions
```python
def add(a, b):
    return a + b

# Lambda function
add_lambda = lambda a, b: a + b

# Function with default argument
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Function with variable arguments
def var_args(*args):
    return sum(args)
```

---

