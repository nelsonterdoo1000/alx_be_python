def perform_operation(num1,num2,operation: str):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise Exception("You cannot divide by zero")
        else:
            return num1 / num2
    else:
        return "You did not enter a valid mathematic operator!"

