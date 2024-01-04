from threatfox import retrieve_data
from threatfox_data_process import process_data
from import_csv import convert_to_json

def run_pipeline():
    # Step 1: Retrieve data
    data = retrieve_data()
    if data:
        # Step 2: Process the data
        process_data(data)

        # Step 3: Convert CSV to JSON
        convert_to_json()

if __name__ == "__main__":
    run_pipeline()
