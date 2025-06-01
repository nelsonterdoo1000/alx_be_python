# script to print the multiplication table of a number



user_input = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{i} * {user_input} = {i * user_input}")
    
          