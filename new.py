import openai
import sqlite3
import pandas as pd
from pdfminer.high_level import extract_text
import re
import PyPDF2


openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "system", "content": prompt}],
        temperature=0.5
    )
    completion_text = response.choices[0].message["content"]
    return completion_text

def extract_data_from_text(pdf_text, metric, metric_keywords):
    prompt = f"""
    Please extract and provide a comprehensive data report on the following sustainability {metric} titles and with its related {metric_keywords} from the provided PDF:
    Please extract all available numerical data, values, and relevant information related to each metric mentioned above from the provided PDF.
    The data report should be well-organized and provide a comprehensive overview of the organization's performance in terms of sustainability and relevant metrics.
    Gather all the data together to its related topic under a single metric.
    """

    completion_text = get_completion(prompt)
    extracted_value = completion_text.strip()
    return extracted_value

def extract_company_info_from_text(pdf_text):
    name = None
    location = None  # Add logic to extract this value
    market_cap = None  # Add logic to extract this value
    website = None  # Add logic to extract this value
    ceo_name = None  # Add logic to extract this value
    report_link = None  # Add logic to extract this value

    name_pattern = r"Company Name:\s*(.*)"
    match = re.search(name_pattern, pdf_text)
    if match:
        name = match.group(1)

    # Similar logic for extracting other information
    return name, location, market_cap, website, ceo_name, report_link



def run_extraction_program(file_paths, metrics, database_file, table_name, output_file):
    # Create a list to store the extracted data for each PDF
    data_list = []

    # Define a dictionary mapping metrics to keywords
    metric_keywords = {
        "Carbon Footprint": ["carbon footprint", "GHG accounting value", "GHG emission", "carbon emission", "carbon impact", "sustainability footprint", "ecological footprint"],
        "Energy Consumption": ["energy consumption", "power usage", "electricity consumption", "energy utilization"],
        "Water Usage": ["water consumption", "water utilization", "water usage"],
        "Waste Generation": ["waste production", "waste generation", "waste output"],
        "Employee Turnover Rate": ["employee turnover rate", "attrition rate", "staff churn"],
        "Diversity Metrics": ["diversity representation", "demographic composition", "inclusivity metrics"],
        "Health and Safety Incidents": ["workplace accidents", "safety records", "incident reports"],
        "Board Diversity": ["board composition", "board demographic", "representation at board level"],
        "CEO-to-Worker Pay Ratio": ["executive-to-staff pay ratio", "income disparity", "wage gap"],
        "Supply Chain Transparency": ["transparency in the supply chain", "supply chain visibility"],
        "Product Safety Incidents": ["safety incidents", "product quality issues", "product recall cases"],
        "Tax Transparency": ["tax disclosure", "tax reporting", "tax payment details"],
        "Innovation Investments": ["research and development spending", "innovation funding"],
        "Employee Training Hours": ["training time", "employee development hours"],
        "Customer Satisfaction Ratings": ["customer feedback", "satisfaction surveys", "customer experience ratings"]
    }

    # Process each PDF file
    for file_path in file_paths:
        # Read the text from the PDF file
        pdf_text = extract_text(file_path)

        # Extract constant information from the PDF
        name, location, market_cap, website, ceo_name, report_link = extract_company_info_from_text(pdf_text)

        # Create a dictionary to store the extracted data for this PDF
        data = {}

        # Add the constant information to the data dictionary
        data['Name'] = name
        data['Location'] = location
        data['Market Cap'] = market_cap
        data['Website'] = website
        data['CEO Name'] = ceo_name
        data['Sustainability Report Link'] = report_link

        # Process each metric
        for metric in metrics:
            if metric in metric_keywords:
                extracted_value = extract_data_from_text(pdf_text, metric, metric_keywords[metric])
                data[metric] = extracted_value
            else:
                print(f"Warning: Metric '{metric}' not found in the metric_keywords dictionary for file '{file_path}'.")


        # Append the data to the list
        data_list.append(data)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)

    # Save data to SQLite table
    conn = sqlite3.connect(database_file)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Data extracted successfully and saved to SQLite table '{table_name}' in '{database_file}'.")

    # Export data to CSV file
    df.to_csv(output_file, index=False)
    print(f"Data exported to '{output_file}'.")


def main(file_paths, metrics, database_file, table_name, output_file):
    # Run the extraction program for the PDF files
    run_extraction_program(file_paths, metrics, database_file, table_name, output_file)

# Define the file paths, metrics, database file, table name, and output file
file_paths = [
    r"C:\Users\Content0010\Downloads\EON_2020_Sustainability_Report.pdf",
    r"C:\Users\Content0010\Downloads\SCR-Report-2021.pdf",
    r"C:\Users\Content0010\Downloads\sustainability-report-en-2021.pdf",
    r"C:\Users\Content0010\Downloads\Sustainability_report2012.pdf",
    r"C:\Users\Content0010\Downloads\EOG_2021_Sustainability_Report.pdf",
    r"C:\Users\Content0010\Downloads\bp-sustainability-report-2021.pdf",
    r"C:\Users\Content0010\Downloads\conocophillips-2021-sustainability-report.pdf",
    r"C:\Users\Content0010\Downloads\petrochina.pdf",
    r"C:\Users\Content0010\Downloads\totall enargy.pdf",
    r"C:\Users\Content0010\Downloads\shell-sustainability-report-2021.pdf",
    r"C:\Users\Content0010\Downloads\chevron-sustainability-report-2022.pdf",
    r"C:\Users\Content0010\Downloads\exxonmobil-sustainability-report.pdf",
    r"C:\Users\Content0010\Downloads\Resilience workshop.pdf",
]

metrics = [
    "Carbon Footprint",
    "Energy Consumption",
    "Water Usage",
    "Waste Generation",
    "Employee Turnover Rate",
    "Diversity Metrics",
    "Health and Safety Incidents",
    "Board Diversity",
    "CEO-to-Worker Pay Ratio",
    "Supply Chain Transparency",
    "Product Safety Incidents",
    "Tax Transparency",
    "Innovation Investments",
    "Employee Training Hours",
    "Customer Satisfaction Ratings"
]
database_file = 'extracted_data.db'
table_name = 'metrics_data'
output_file = r'C:\Users\Content0010\Desktop\aramco.csv'

# Run the main program
main(file_paths, metrics, database_file, table_name, output_file)
