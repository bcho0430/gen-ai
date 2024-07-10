import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.baseball-reference.com/teams/OAK/2024-schedule-scores.shtml#all_results"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

df = pd.DataFrame(columns=['Date', 'Opponent'])

table = soup.find_all('table')
for row in table[0].tbody.find_all('tr'):
    columns = row.find_all('td')
    try:
        date = columns[0].text
        at = columns[3].text
        opponent = columns[4].text
    except:
        pass
    if at == '':
        df = df._append({'Date': date, 'Opponent':opponent}, ignore_index=True)

csv_file_path = "oakland_athletics24.csv"

df.to_csv(csv_file_path, index=False)