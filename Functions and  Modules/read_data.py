def read_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.readlines()
        print(f"Data successfully read from {file_path}.")
        return data
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []
