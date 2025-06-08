def perform_operation(num1, num2, operation):
    """
    Perform arithmetic operation on two numbers.
    
    Args:
        num1: First number
        num2: Second number
        operation: String indicating the operation ('+', '-', '*', '/')
        
    Returns:
        Result of the arithmetic operation
        
    Raises:
        ValueError: If operation is not supported
        ZeroDivisionError: If division by zero is attempted
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise Exception("You cannot divide by zero")
        return num1 / num2
    else:
        return "You did not enter a valid mathematic operator!" 