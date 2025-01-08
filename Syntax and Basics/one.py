import math

def one():
    try:
        shape = input("Enter the shape (square, rectangle, parallelogram, triangle, circle): ").strip().lower()

        if shape == "square":
            side = float(input("Enter the side length "))
            area = side ** 2
            perimeter = 4 * side
            print(f"Square - Area: {area}, Perimeter: {perimeter}")

        elif shape == "rectangle":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length * width
            perimeter = 2 * (length + width)
            print(f"Rectangle - Area: {area}, Perimeter: {perimeter}")

        elif shape == "parallelogram":
            base = float(input("Enter the base length of the parallelogram: "))
            side = float(input("Enter the side length of the parallelogram: "))
            area = base * side
            perimeter = 2 * (base + side)
            print(f"Parallelogram - Area: {area}, Perimeter: {perimeter}")

        elif shape == "triangle":
            a = float(input("Enter the length of the first side of the triangle: "))
            b = float(input("Enter the length of the second side of the triangle: "))
            c = float(input("Enter the length of the third side of the triangle: "))
            
            # Check if the sides form a valid triangle
            if a + b > c and a + c > b and b + c > a:
                perimeter = a + b + c
                s = perimeter / 2
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                print(f"Triangle - Area: {area:.2f}, Perimeter: {perimeter}")

            else:
                print("Invalid triangle! The sum of any two sides must be greater than the third side.")
        


        elif shape == "circle":
            radius = float(input("Enter the radius of the circle: "))
            area = math.pi * radius ** 2
            perimeter = 2 * math.pi * radius
            print(f"Circle - Area: {area:.2f}, Circumference: {perimeter:.2f}")

        else:
            print("Invalid shape! Please enter a valid shape name (square, rectangle, parallelogram, triangle, circle).")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

one()
