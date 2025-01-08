import math

def three():
    try: 
        principal=int(input("Enter the principal amount:"))
        rate=int(input("Enter the rate of interest annually: "))
        tenure=int(input("Enter time period of loan(in years): "))
        interest=(principal*rate*tenure)/100
        print(interest)

    except ValueError:
        print("Invalid input! Please enter numeric values.")

three()