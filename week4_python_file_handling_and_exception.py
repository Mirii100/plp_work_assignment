
print('i want to  assignment on  File Handling and Exception Handling Assignment ')
def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, "r") as f:
            content = f.readlines()

        # Modify content (example: converting to uppercase)
        modified_content = [line.lower() for line in content]

        with open(output_filename, "w") as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print("Error: An issue occurred while reading or writing the file.")

def main():
    filename = input("Enter the filename to read: ")
    output_file = "modified_" + filename  # Creating a modified output file

    read_and_modify_file(filename, output_file)

if __name__ == "__main__":
    main()
