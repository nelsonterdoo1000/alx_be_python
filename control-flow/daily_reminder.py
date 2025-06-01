# script to  remind the user of activities based on priority and time-boundedness


task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

while True:
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task that requires attention at your earliest convenience.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires attention today!")
            else:
                print(f"Reminder: '{task}' is a medium priority task that requires attention at your earliest convenience.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task that requires attention today!")
            else:
                print(f"Reminder: '{task}' is a low priority task that requires attention at your earliest convenience.")
        case _:
            print("Invalid priority level.")
    break