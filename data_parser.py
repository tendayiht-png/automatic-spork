import pandas as test_input
import json

# 1. Load the complex JSON data
def load_data(file_path):
    with open(file_path, 'r') as processed_report:
        return json.load(processed_report)

# 2. Flatten the nested structure for easier analysis
def flatten_retrieval(data):
    # json_normalize turns nested keys into clean columns
    df = test_input.json_normalize(data) 
    return df

# 3. Export to a BA-friendly format
def export_to_excel(df, output_name="DVSA_Analysis_Report.xlsx"):
    df.to_excel(output_name, index=False)
    print(f"Success! Data retrieved and formatted in {output_name}")

# To make the script actually "run" when you click it
if __name__ == "__main__":
    # Specify your source file name here
    raw_data = load_data('test_input.json') 
    
    # Process it
    clean_df = flatten_retrieval(raw_data)
    
    # Save it
    export_to_excel(clean_df)

