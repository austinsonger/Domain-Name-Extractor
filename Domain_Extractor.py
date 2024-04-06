import pandas as pd
from duckduckgo_search import DDGS
import csv
import asyncio
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def find_company_url(company_name):
    """
    Find the most likely corporate URL for a given company name using DuckDuckGo.
    """
    ddgs = DDGS()
    results = ddgs.text(company_name + " corporate website", max_results=1)
    if results:
        # Assuming the first result is the most relevant one
        company_url = results[0]['href']
    else:
        company_url = "URL Not Found"
    
    return company_url

def main(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Assuming the column with company names is named 'Company Name'
    company_names = df['Company Name'].tolist()
    
    # Initialize a list to store dictionaries of company names and URLs
    data = []
    
    for name in company_names:
        url = find_company_url(name)
        data.append({'Company Name': name, 'Corporate URL': url})
    
    # Convert the list of dictionaries to a DataFrame
    new_df = pd.DataFrame(data)
    
    # Export to CSV
    new_df.to_csv('company_urls_with_websites.csv', index=False)
    print("Exported to company_urls_with_websites.csv")

# Path to the CSV file with company names
csv_file_path = "company_urls - Sheet1 (1).csv"

if __name__ == "__main__":
    main(csv_file_path)
