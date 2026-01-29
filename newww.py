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

# students above average
above_average = []
for name, score in students.items():
    if score > average:
        above_average.append(name)

# grade logic
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

# pass / fail logic
def get_status(score):
    return "Pass" if score >= 40 else "Fail"

# grade assignment
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

print("Student Score Report")
print("--------------------")
print("Average score:", round(average, 2))
print("Topper:", topper_name, "with", topper_score, "marks")

# summary
pass_count = 0
for score in students.values():
    if score >= 40:
        pass_count += 1

print("\nGrades:")
for name, score in students.items():
    print(name, ":", get_grade(score))

print("\nStudents above average:")
for student in above_average:
    print("-", student)

print("\nAll students (sorted by score):")
for name, score in sorted(students.items(), key=lambda x: x[1], reverse=True):
    print(name, ":", score)








