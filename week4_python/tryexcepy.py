try:
    with open(r'openfile.py', 'r') as file:
        # Read the contents of the file
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The file was not found. Please check the file path.")