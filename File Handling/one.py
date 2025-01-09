import pandas as pd

try:
    file_path = '/Users/consultadd/Desktop/File Handling/sales_data_sample.csv'
    data = pd.read_csv(file_path, encoding='ISO-8859-1')
    print(data.head())
except Exception as e:
    print(f"An error occurred: {e}")
