# grade_checker.py
# A simple program that calculates a student's grade based on their numeric score.

def check_grade(score):
    """
    Returns letter grade based on numeric score:
    90+      = A
    80 - 89  = B
    70 - 79  = C
    60 - 69  = D
    Below 60 = F
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    try:
        # Prompt the user to enter a score
        score_input = input("Enter your score: ")
        score = float(score_input)

        # Validate score range
        if score < 0 or score > 100:
            print("Please enter a score between 0 and 100.")
        else:
            # Determine grade and display the result
            grade = check_grade(score)
            print(f"Grade: {grade}")

    except ValueError:
        # Handle non-numeric input gracefully
        print("Invalid input! Please enter a valid number.")

# Run the grade checker program
if __name__ == "__main__":
    main()
