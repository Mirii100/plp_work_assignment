# Open the file in read mode
file_path = "example.txt"  # Replace with your file path
try:
    with open(file_path, "r") as file:
        # Read the content of the file
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")