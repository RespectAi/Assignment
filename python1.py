# Ask the user for two numbers and a mathematical operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operation (+, -, *, /): ")

# Perform the chosen operation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero!")
        exit()
else:
    print("Invalid operation!")
    exit()

# Display the result
print(f"{num1} {operator} {num2} = {result}")
5