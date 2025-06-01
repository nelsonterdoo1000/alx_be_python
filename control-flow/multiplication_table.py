# script to print the multiplication table of a number

user_input = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    print(f"{user_input} * {i} = {user_input * i}")