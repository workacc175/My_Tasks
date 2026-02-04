#task b

# 1. Create a list of dictionaries representing students
students = [
    {"name": "Alice", "grades": [85, 90, 92]},
    {"name": "Bob", "grades": [78, 81, 74]},
    {"name": "Charlie", "grades": [95, 88, 91]}
]

# 2. Write a script to calculate and print results
print("--- Student Grade Reports ---")

for student in students:
    # Access the list of grades for the current student
    grades_list = student["grades"]
    
    # Calculate the average grade
    # formula: sum of items / number of items
    average = sum(grades_list) / len(grades_list)
    
    # Print the name and the formatted average grade
    print(f"Student: {student['name']} | Average: {average:.2f}")