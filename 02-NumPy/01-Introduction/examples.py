import numpy as np

# 1. Create a 1D array
a = np.array([10, 20, 30, 40, 50])

print("Array:", a)
print("Dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)

# 2. Create a 2D array
b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n2D Array:")
print(b)

print("5:", b[1, 1])
print("8:", b[2, 1])
print("Shape:", b.shape)
print("Dimensions:", b.ndim)

# 3. Array operations
x = np.array([10, 20, 30])
y = np.array([2, 4, 5])

print("\nAddition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

# 4. Basic statistical functions
print("\nSum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))