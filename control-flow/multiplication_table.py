# script to print the multiplication table of a number

user_input = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    #declare the product variable
    product = user_input * i
    
    #print the product
    print(f"{user_input} * {i} = {product}")