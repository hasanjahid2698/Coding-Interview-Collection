## ✅ 1. **Recursion Tree Method**

### 📌 Use When:

* You want to **visualize** how the recursive calls grow.
* The recurrence is not easily solvable using formulas (e.g., not easily matching Master Theorem format).

### 🧠 Idea:

Break down each recursive call into its child calls and calculate the **work done at each level**, then sum across all levels.

### 📘 Example:

```python
def func(n):
    if n <= 1:
        return 1
    return func(n//2) + func(n//2) + n
```

### Step-by-step:

* Recurrence:
  $T(n) = 2T(n/2) + O(n)$

* Level 0: $n$ work

* Level 1: 2 calls, each with $n/2$ → Total work: $2 \cdot (n/2) = n$

* Level 2: 4 calls, each with $n/4$ → Total work: $4 \cdot (n/4) = n$

* ...

* Log₂(n) levels.

**Total work = n + n + n + ... + n (log n times) = O(n log n)**

---

## ✅ 2. **Substitution (Iteration) Method**

### 📌 Use When:

* You want to **derive** the time complexity by expanding the recurrence step-by-step.

### 🧠 Idea:

Repeatedly substitute the recurrence into itself until you find a pattern, then generalize.

### 📘 Example:

```python
def func(n):
    if n <= 1:
        return 1
    return func(n - 1) + 1
```

### Steps:

* $T(n) = T(n-1) + 1$
* $T(n-1) = T(n-2) + 1$
* ...
* $T(1) = 1$

Substitute:

$$
T(n) = T(n-1) + 1 = T(n-2) + 2 = \ldots = T(1) + (n - 1) = 1 + (n - 1) = O(n)
$$

---

## ✅ 3. **Master Theorem**

### 📌 Use When:

* The recurrence is in the **form**:

  $$
  T(n) = aT(n/b) + f(n)
  $$

  Where:

  * `a` = number of recursive calls
  * `n/b` = size of each subproblem
  * `f(n)` = work done outside the recursive calls

### 🧠 Cases:

Let $f(n) = \Theta(n^d)$:

* **Case 1:** If $a > b^d$ → $T(n) = \Theta(n^{\log_b a})$
* **Case 2:** If $a = b^d$ → $T(n) = \Theta(n^d \log n)$
* **Case 3:** If $a < b^d$ → $T(n) = \Theta(n^d)$

### 📘 Example:

```python
def merge_sort(arr):
    ...
    merge_sort(left)
    merge_sort(right)
    merge(...)
```

* Recurrence: $T(n) = 2T(n/2) + O(n)$
* Here, $a = 2, b = 2, f(n) = n \Rightarrow d = 1$
* $a = b^d \Rightarrow$ Case 2 →
  ✅ $T(n) = O(n \log n)$

---

## ✅ 4. **Recursion Depth + Work per Call**

### 📌 Use When:

* The recursion is straightforward (e.g., linear).
* Each level does constant or predictable work.

### 🧠 Idea:

* Time = **Depth of recursion × Work per call**

### 📘 Example:

```python
def print_n(n):
    if n == 0:
        return
    print(n)
    print_n(n - 1)
```

* Depth = $n$
* Work per call = $O(1)$
* ⇒ $O(n)$

---

## 🧰 Summary Table

| Method                | Best For                                      |
| --------------------- | --------------------------------------------- |
| Recursion Tree        | Visualization, summing per level              |
| Substitution          | Deriving pattern manually                     |
| Master Theorem        | Divide-and-conquer in $T(n) = aT(n/b) + f(n)$ |
| Recursion Depth Model | Simple linear or tail recursion               |

---
