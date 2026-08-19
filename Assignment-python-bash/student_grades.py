# student_grades.py
# A simple dictionary-based student grade management system.

def main():
    # Dictionary to store student names as keys and grades as values
    student_grades = {}

    # Menu loop until user exits
    while True:
        print("\n===== Student Grades =====")
        print("1. Add Student")
        print("2. Update Grade")
        print("3. Display All Students")
        print("4. Exit")

        # Get user menu choice
        choice = input("\nEnter your choice: ").strip()

        # Option 1: Add a new student and grade
        if choice == "1":
            name = input("Enter student name: ").strip()
            grade = input("Enter student grade: ").strip()
            # Store student name and grade in dictionary
            student_grades[name] = grade
            print(f"Student '{name}' added successfully.")

        # Option 2: Update existing student's grade
        elif choice == "2":
            name = input("Enter student name: ").strip()
            # Check if student exists in dictionary using if / else
            if name in student_grades:
                new_grade = input("Enter new grade: ").strip()
                student_grades[name] = new_grade
                print(f"Grade updated for '{name}'.")
            else:
                print("Student not found.")

        # Option 3: Display all students using a loop
        elif choice == "3":
            if not student_grades:
                print("No student records found.")
            else:
                print()
                # Loop through dictionary items and display name and grade
                for name, grade in student_grades.items():
                    print(f"{name} : {grade}")

        # Option 4: Exit program
        elif choice == "4":
            print("Exiting Student Grades program. Goodbye!")
            break

        # Handle invalid choices
        else:
            print("Invalid choice! Please select an option between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()
