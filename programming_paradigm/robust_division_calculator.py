def safe_divide(numerator, denominator):
    """
    Safely performs division with robust error handling.
    
    Args:
        numerator: The dividend (can be string or numeric)
        denominator: The divisor (can be string or numeric)
    
    Returns:
        str: Result of division or appropriate error message
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Perform division
        result = num / den
        return f"The result of the division is {result}"
        
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"