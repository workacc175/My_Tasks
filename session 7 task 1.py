import numpy as np

# 1. Create Arrays
A = np.array([10, 20, 30, 40, 50])
B = np.array([5, 4, 3, 2, 1])

# 2. Perform Operations
addition = A + B
subtraction = A - B
multiplication = A * B
division = A / B

# 3. Apply NumPy Functions
mean_A = np.mean(A)
max_A = np.max(A)
min_A = np.min(A)

dot_product = np.dot(A, B)
reshaped_A = A.reshape(5, 1)

# --- Displaying Results ---
print("Array A:", A)
print("Array B:", B)
print("-" * 30)
print("Addition (A + B):", addition)
print("Subtraction (A - B):", subtraction)
print("Multiplication (A * B):", multiplication)
print("Division (A / B):", division)
print("-" * 30)
print(f"Stats for A: Mean={mean_A}, Max={max_A}, Min={min_A}")
print("Dot Product of A and B:", dot_product)
print("Reshaped A (5x1):\n", reshaped_A)