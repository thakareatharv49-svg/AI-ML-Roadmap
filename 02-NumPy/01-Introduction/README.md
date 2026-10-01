# NumPy — Introduction & Basics

## 1. What is NumPy?

NumPy stands for **Numerical Python**.

It is a Python library used for:

* Numerical computation
* Arrays
* Matrices
* Mathematical operations
* Scientific computing
* Data manipulation

NumPy is important in AI/ML because machine-learning data is largely represented as numerical arrays.

---

## 2. Importing NumPy

```python
import numpy as np
```

`np` is the standard short name used for NumPy.

---

## 3. Creating a NumPy Array

```python
import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a)
```

Output:

```text
[10 20 30 40 50]
```

---

## 4. 1D Array

```python
a = np.array([10, 20, 30, 40, 50])
```

This is a **1-dimensional array**.

```python
print(a.ndim)
```

Output:

```text
1
```

---

## 5. 2D Array

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

This is a **2-dimensional array**.

```python
print(a.ndim)
```

Output:

```text
2
```

---

## 6. `ndim`

`ndim` returns the number of dimensions of an array.

```python
a = np.array([1, 2, 3])

print(a.ndim)
```

Output:

```text
1
```

---

## 7. `shape`

`shape` tells us the size of each dimension.

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.shape)
```

Output:

```text
(2, 3)
```

Meaning:

```text
2 rows
3 columns
```

---

## 8. `size`

`size` returns the total number of elements.

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.size)
```

Output:

```text
6
```

Because:

```text
2 × 3 = 6
```

---

## 9. Indexing

NumPy uses **zero-based indexing**.

```python
a = np.array([10, 20, 30, 40])

print(a[0])
print(a[2])
```

Output:

```text
10
30
```

### 2D indexing

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a[1, 1])
```

Output:

```text
5
```

Syntax:

```python
array[row, column]
```

---

## 10. Basic Array Operations

```python
a = np.array([10, 20, 30])
b = np.array([2, 4, 5])
```

### Addition

```python
print(a + b)
```

Output:

```text
[12 24 35]
```

### Subtraction

```python
print(a - b)
```

Output:

```text
[ 8 16 25]
```

### Multiplication

```python
print(a * b)
```

Output:

```text
[ 20  80 150]
```

### Division

```python
print(a / b)
```

Output:

```text
[5. 5. 6.]
```

---

## 11. Basic Statistical Functions

```python
a = np.array([10, 20, 30, 40])
```

### Sum

```python
np.sum(a)
```

Result:

```text
100
```

### Mean

```python
np.mean(a)
```

Result:

```text
25.0
```

### Maximum

```python
np.max(a)
```

Result:

```text
40
```

### Minimum

```python
np.min(a)
```

Result:

```text
10
```

---

## Important Concepts

| Function / Attribute | Purpose                  |
| -------------------- | ------------------------ |
| `np.array()`         | Creates a NumPy array    |
| `ndim`               | Number of dimensions     |
| `shape`              | Size of each dimension   |
| `size`               | Total number of elements |
| `np.sum()`           | Sum of elements          |
| `np.mean()`          | Average                  |
| `np.max()`           | Maximum value            |
| `np.min()`           | Minimum value            |

---

## Common Mistakes

### Wrong

```python
np.arrays([1, 2, 3])
```

### Correct

```python
np.array([1, 2, 3])
```

---

### Wrong

```python
a.[1, 2]
```

### Correct

```python
a[1, 2]
```

---

## AI/ML Connection

NumPy arrays are the foundation for numerical data in machine learning.

A dataset can be represented as a matrix:

```text
        Feature 1  Feature 2  Feature 3
Sample 1    10        20        30
Sample 2    40        50        60
Sample 3    70        80        90
```

This can be represented using a NumPy 2D array.

Understanding:

```text
array
ndim
shape
size
indexing
operations
```

is therefore essential before moving into Pandas and Machine Learning.
