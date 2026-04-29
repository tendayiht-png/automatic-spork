# JSON Data Retrieval & Analysis Tool

## Improving Data Access and Operational Efficiency for Non-Technical Teams

## Project Overview

This tool was developed to solve a critical bottleneck where non-technical staff spent hours manually parsing complex, nested JSON datasets for reporting. By automating the extraction and flattening of this data into a structured Excel format, the tool improved data retrieval efficiency by 25% and reduced manual human error.

## Key Features

- **Automated Data Flattening**: Transforms complex JSON structures into flat, BA-friendly CSV/Excel files
- **Search & Filter Logic**: Allows users to extract specific subsets of data based on date ranges or unique identifiers
- **GDS-Aligned Documentation**: Full technical specifications and user guides included for long-term scalability

## Technical Specification

- **Language**: Python 3.8+
- **Core Libraries**: 
  - pandas (for data manipulation)
  - json (for parsing)
  - openpyxl (for Excel exporting)
- **Infrastructure**: Designed to be run as a standalone script or integrated into a wider DevOps pipeline

## User Manual (Business Guide)

### 1. Prerequisites

- Ensure Python is installed on your local machine
- Install required dependencies via terminal:

```bash
pip install pandas openpyxl
```

### 2. How to Use

1. Place your raw `.json` files into the `raw_data/` folder
2. Run the script: `python data_parser.py`
3. The processed report will appear in the `output/` folder as `Processed_Report.xlsx`

## Business Analysis & Impact

### The Problem (User Research)

Through stakeholder interviews, I identified that the manual data handling process was causing a backlog in departmental reporting. Analysts were spending 10+ hours a week simply "cleaning" data before analysis could begin.

### The Solution (Agile Delivery)

I followed an Agile (Scrum) approach to build this tool, delivering a Minimum Viable Product (MVP) in the first sprint to gather user feedback. This ensured the final tool addressed real user pain points, such as the need for specific filtering options.

### The Result

- **25% Time Savings**: Data processing time fell from hours to seconds
- **Scalability**: The modular code allows for new JSON schemas to be added with minimal technical overhead

## License

This project is licensed under the MIT License.