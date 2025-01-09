def save_results(data, output_file):
    with open(output_file, 'w') as file:
        file.writelines(data)
    print(f"Results saved to {output_file}.")

def display_results(data):
    print("Displaying results:")
    for line in data:
        print(line)
