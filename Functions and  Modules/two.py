import read_data
import process_data
import report_results

def main():
    # Fetch the data from a file
    data = read_data.read_data('data.txt')
    
    if not data:
        return 
    
    filtered_data = process_data.filter_data(data, 'Hello')  
    transformed_data = process_data.transform_data(filtered_data)
    
    report_results.display_results(transformed_data)
    report_results.save_results(transformed_data, 'output.txt')

main()
