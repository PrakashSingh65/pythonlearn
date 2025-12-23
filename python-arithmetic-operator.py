def calculator():
    num1 = float(input("Enter first number: "))
    operation = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operation == '+':
        print(f"{num1}+{num2}={num1 + num2}")
    elif operation == '-':
        print(f"{num1}-{num2}={num1 - num2}")
    elif operation == '*':
        print(f"{num1}*{num2}={num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"{num1}/{num2}={num1 / num2}")
        else:
            print("Error: Division by zero")
    else:
        print("invalid operation")
        
calculator()