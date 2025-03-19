

with open("example.txt", "r+") as f: 
    data = f.write('are you ther e?') 
    details=f.read()
    print(data)
    print(details)