### **1. Basics of Bit Manipulation**

* **Binary Representation**: Understanding how numbers are represented in binary.
* **Bitwise Operators**: Learn basic operators: AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and Shift operations (`<<`, `>>`).

---

### **2. Common Bit Manipulation Tricks**

1. **Checking if a number is odd or even**:

   ```python
   if (n & 1):  # Odd
   else:  # Even
   ```

2. **Checking if the `i-th` bit is set**:

   ```python
   if (n & (1 << i)):
   ```

3. **Setting the `i-th` bit**:

   ```python
   n |= (1 << i)
   ```

4. **Clearing the `i-th` bit**:

   ```python
   n &= ~(1 << i)
   ```

5. **Toggling the `i-th` bit**:

   ```python
   n ^= (1 << i)
   ```

6. **Counting the number of set bits**:

   * Use **Brian Kernighan's Algorithm**:

     ```python
     count = 0
     while n:
         n &= (n - 1)
         count += 1
     ```

---

### **3. Specialized Algorithms**

1. **Finding the Only Non-Repeating Element (XOR)**:

   * For an array where every element appears twice except one:

     ```python
     result = 0
     for num in arr:
         result ^= num
     ```

2. **Finding Two Non-Repeating Elements**:

   * Use XOR and bit masking to separate elements into two groups.

3. **Checking if a number is a power of 2**:

   ```python
   if (n & (n - 1)) == 0:
   ```

4. **Swapping two numbers without a temporary variable**:

   ```python
   a = a ^ b
   b = a ^ b
   a = a ^ b
   ```

5. **Reversing Bits**:

   ```python
   def reverse_bits(n):
       result = 0
       for _ in range(32):  # Assuming 32-bit integer
           result = (result << 1) | (n & 1)
           n >>= 1
       return result
   ```

---

### **4. Optimization Techniques**

1. **Extracting the Lowest Set Bit**:

   ```python
   low_bit = n & -n
   ```

2. **Clearing the Lowest Set Bit**:

   ```python
   n &= (n - 1)
   ```

3. **Getting the Log Base 2 (Position of Most Significant Bit)**:

   ```python
   import math
   msb_position = math.floor(math.log2(n))
   ```

4. **Generate All Subsets of a Set Using Bits**:

   ```python
   n = len(arr)
   for i in range(1 << n):
       subset = [arr[j] for j in range(n) if (i & (1 << j))]
   ```

---

### **5. Advanced Concepts**

1. **Bitmask Dynamic Programming**:

   * Often used in problems like the Traveling Salesman Problem or subset-related problems.

2. **Gray Code Generation**:

   ```python
   gray_code = n ^ (n >> 1)
   ```

3. **Hamming Distance Between Two Numbers**:

   ```python
   def hamming_distance(x, y):
       return bin(x ^ y).count('1')
   ```

4. **Finding the Missing Number in an Array**:

   * XOR all array elements and indices.

5. **Divide and Multiply by Powers of 2**:

   * Left shift for multiplication, right shift for division:

     ```python
     result = n << k  # Multiply by 2^k
     result = n >> k  # Divide by 2^k
     ```

---

### **6. System-Level Tricks**

1. **Endian Conversion**:

   * Swap bytes to change the endianness of a number.

2. **Bit Packing and Unpacking**:

   * Pack multiple small integers into a single integer and unpack them.

3. **Efficient Computation of Modulo (Power of Two)**:

   ```python
   remainder = n & (m - 1)  # For m = 2^k
   ```
