from statistics import mean, median, mode, stdev

def two():
    try:
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        if not numbers:
            print("No numbers provided.")
            return
        
        print(f"Mean: {mean(numbers):.2f}")
        print(f"Median: {median(numbers):.2f}")
        print(f"Mode: {mode(numbers):.2f}")
        print(f"Standard Deviation: {stdev(numbers):.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except StatisticsError as e:
        print(f"Error: {e}")

two()
