# prompting user to enter numbers 
print('enter two numbers  ')
print('enter first number  ')
num1=int(input())

print('enter second number ')
num2=int(input())

operation = input("Enter an operation (+, -, *, /): ")

if operation == '+':
            
            result = num1 + num2
            print('result is   ',result)
elif operation == '-':
            result = num1 - num2
            print('result is   ',result)
elif operation == '*':
            result = num1 * num2
            print('result is   ',result)
elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print('result is   ',result)
            else:
                print("Error: Division by zero is not allowed.")
                
else:
            print("Invalid operation. Please enter +, -, *, or /.")
            
