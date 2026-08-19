# file_write.py
# A beginner-friendly program demonstrating file writing in Python.

import os

def main():
    # Define directory and file path
    data_dir = "data"
    file_path = os.path.join(data_dir, "sample.txt")

    # Ensure the 'data/' folder exists before creating the file
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Text content to write into the file
    content = (
        "Hello, this is my Python file handling assignment.\n"
        "This file was created using Python.\n"
    )

    # Open the file in write mode ('w') using 'with' block
    # 'with' automatically closes the file after writing
    with open(file_path, "w") as file:
        file.write(content)

    print(f"Successfully wrote content to '{file_path}'.")

# Run the file write program
if __name__ == "__main__":
    main()
