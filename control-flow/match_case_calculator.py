# using match case to create a calculator
#
# 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "/":
        if num1  == 0 or num2 == 0:
            print("Error: Division by zero")
        else:
            print(f"The result is {num1 / num2}")
    case _:
        print("Error: Invalid operation")
