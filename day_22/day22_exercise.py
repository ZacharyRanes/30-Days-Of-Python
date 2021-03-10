# Scrape the presidents table and store the data as json
# (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States)

import json
import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')
tables = soup.find_all('table')

for table in tables:
    for td in table.find('tr').find_all('td'):
        print(td.text)

# data = json.loads(tables)

# with open('data.json', 'w') as my_data_file:
#     json.dump(data, my_data_file)
