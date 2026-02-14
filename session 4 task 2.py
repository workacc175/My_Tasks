def calculator(a, b, operation):
    # 1. Addition
    if operation == "add":
        return a + b
    
    # 2. Subtraction
    elif operation == "subtract":
        return a - b
    
    # 3. Multiplication
    elif operation == "multiply":
        return a * b
    
    # 4. Division
    elif operation == "divide":
        # Always check for division by zero to avoid crashing!
        if b == 0:
            return "Error: Cannot divide by zero."
        return a / b
    
    # 5. Fallback for invalid operation strings
    else:
        return "Invalid operation provided."

# Testing the function:
print(calculator(10, 5, "add"))       # Output: 15
print(calculator(10, 5, "divide"))    # Output: 2.0
print(calculator(10, 0, "divide"))    # Output: Error: Cannot divide by zero.