# main.py
import numpy as np
from math_operations import MathOperations

def get_matrix_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    print(f"Enter the elements of the {rows}x{cols} matrix row by row:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

def main():
    print("Math Operations Program")
    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Matrix Multiplication")
        print("4. Exit")

        choice = int(input("Enter choice (1-4): "))

        if choice == 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = MathOperations.add(a, b)
            print(f"Result: {result}")

        elif choice == 2:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = MathOperations.subtract(a, b)
            print(f"Result: {result}")

        elif choice == 3:
            print("Enter first matrix:")
            matrix1 = get_matrix_input()
            print("Enter second matrix:")
            matrix2 = get_matrix_input()
            result = MathOperations.multiply_matrices(matrix1, matrix2)
            print(f"Result of matrix multiplication:\n{result}")

        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

main()
