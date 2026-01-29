students = {
    "Amit": 78,
    "Neha": 85,
    "Ravi": 92,
    "Priya": 88
}

# calculate average
total = sum(students.values())
average = total / len(students)

# find topper
topper_name = max(students, key=students.get)
topper_score = students[topper_name]

print("Student Score Report")
print("--------------------")
print("Average score:", average)
print("Topper:", topper_name, "with", topper_score, "marks")
