def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input, please enter an integer.")
        exit(1)

    if is_prime(n) :
        print(f"{n} is prime")
    else:
        print(f"{n} is not priime")