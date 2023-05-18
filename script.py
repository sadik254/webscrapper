import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    # Perform web scraping for the given URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Process and store the scraped data as needed
    table_data = []

    # Extract the desired data
    th_element = soup.find('th', class_='p-3')
    if th_element:
        label = th_element.text.strip()
        table_data.append(('Company Name', label))

    # Extract data from each tab
    tabs = soup.find('ul', class_='nav nav-tabs').find_all('a', class_='nav-link')
    for tab in tabs:
        tab_id = tab['data-target']
        tab_content = soup.find('div', class_='tab-content').find('div', id=tab_id[1:])
        if tab_content:
            # Extract data from the tables in the tab
            tables = tab_content.find_all('table')
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    label_element = row.find('th')
                    value_element = row.find('td')
                    if label_element and value_element:
                        label = label_element.text.strip()
                        value = value_element.text.strip()
                        table_data.append((label, value))

    return table_data

# URL to scrape (replace with your desired URL)
url = 'https://www.bgmea.com.bd/member/2'

# Call the scrape_data function with the single URL
data = scrape_data(url)

# Print or process the scraped data
if data:
    for item in data:
        label, value = item
        print(f"{label}: {value}")
else:
    print("No data found.")

print("Script execution completed.")