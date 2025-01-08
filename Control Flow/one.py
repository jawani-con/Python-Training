import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    try:
        n = int(input("Enter a number: "))
        if n <= 0:
            print("Neither prime nor composite.")
        elif is_prime(n):
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is a composite number.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

main()
