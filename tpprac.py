# student_marks.py

students = {
    "Rahul": 85,
    "Anita": 92,
    "Suresh": 78,
    "Meena": 88
}

# Calculate average marks
average = sum(students.values()) / len(students)

# Find topper
topper = max(students, key=students.get)

print("Average Marks:", average)
print("Topper:", topper, "with", students[topper], "marks")


# list_stats.py

numbers = [10, 20, 30, 40, 50]

print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

# random_numbers.py

import random

numbers = [random.randint(1, 100) for _ in range(5)]
print("Generated numbers:", numbers)
