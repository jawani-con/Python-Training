def filter_data(data, keyword):
    filtered_data = [line.strip() for line in data if keyword in line]
    print(f"Data filtered with keyword: {keyword}.")
    return filtered_data

def transform_data(data):
    """Function to transform data (e.g., converting to uppercase)."""
    transformed_data = [line.upper() for line in data]
    print("Data transformed to uppercase.")
    return transformed_data
