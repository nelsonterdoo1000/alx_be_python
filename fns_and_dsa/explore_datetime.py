from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Calculate and display a future date based on user input for number of days to add.
    """
    # Prompt user for number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Get current date and calculate future date
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    
    # Print the future date in YYYY-MM-DD format
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    """
    Main function to execute both parts of the datetime exploration.
    """
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate future date
    calculate_future_date()

if __name__ == "__main__":
    main()