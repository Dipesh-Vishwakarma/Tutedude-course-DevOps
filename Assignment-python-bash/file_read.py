# file_read.py
# A beginner-friendly program demonstrating how to read a file in Python.

import os

def main():
    # Define path to the text file
    file_path = os.path.join("data", "sample.txt")

    # Verify if file exists before trying to read it
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist. Please run file_write.py first.")
        return

    # Open the file in read mode ('r') using 'with' statement
    with open(file_path, "r") as file:
        # Use file.read() to read the full contents of the file
        content = file.read()

    # Display formatted file contents
    print("===== File Content =====\n")
    print(content)

# Run the file read program
if __name__ == "__main__":
    main()
