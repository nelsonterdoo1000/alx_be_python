# script to print the multiplication table of a number

number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    #declare the product variable
    product = number * i
    
    #print the product
    print(f"{number} * {i} = {product}")