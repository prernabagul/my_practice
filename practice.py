class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self):
        name = input("Enter student name: ").title()
        marks = int(input("Enter marks: "))
        self.students[name] = marks
        print("Student added successfully")

    def remove_student(self):
        name = input("Enter student name to remove: ").title()
        if name in self.students:
            del self.students[name]
            print("Student removed successfully")
        else:
            print("Student not found")

    def view_students(self):
        if not self.students:
            print("\nNo students available")
            return

        print("\nStudent List:")
        for name, marks in self.students.items():
            print(name, "-", marks)

    def search_student(self):
        name = input("Enter student name to search: ").title()
        if name in self.students:
            print(name, "scored", self.students[name])
        else:
            print("Student not found")

    def calculate_average(self):
        if not self.students:
            print("No students to calculate average")
            return

        total = sum(self.students.values())
        average = total / len(self.students)
        print("Class Average:", round(average, 2))


# -------- MAIN PROGRAM --------
manager = StudentManager()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Students")
    print("4. Search Student")
    print("5. Calculate Average")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        manager.add_student()
    elif choice == "2":
        manager.remove_student()
    elif choice == "3":
        manager.view_students()
    elif choice == "4":
        manager.search_student()
    elif choice == "5":
        manager.calculate_average()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again")
