# Script to draw a pattern based on user input

#get user input

pattern = int(input("Enter the size of the pattern: "))
while True:
    for i in range (1, pattern + 1):
        for j in range (1, pattern + 1):
            print("*", end="")
        print()
    break
