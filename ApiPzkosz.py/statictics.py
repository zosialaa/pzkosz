import requests
import pandas as pd
from bs4 import BeautifulSoup
import openpyxl  # import to excel
from tabulate import tabulate  # format

url = "https://rozgrywki.pzkosz.pl/liga/4/statystyki.html"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
if "Łapiński" in r.text:
    print("JEEEEST")

table = soup.find("table", class_="stattype splitTable").find(
    'tbody').find_all('tr')

#print(table)
table_data = []

for row in table:
    dic = {}

    row_data = row.find_all('td')
    dic['place'] = row_data[0].text
    dic['player'] = row_data[1].text
    dic['team'] = row_data[2].text
    dic['matches'] = row_data[3].text
    dic['points_sum'] = row_data[4].text
    dic['points_avg'] = row_data[5].text

    table_data.append(dic)

#print(table_data)
# for key, value in dic.items():
#   table.append([key, value])

headers = table_data[0].keys()
print(tabulate(table_data, headers="keys"))


# , tablefmt="grid"

df = pd.DataFrame(table_data)
df.to_excel('teams_data.xlsx', index=False)
df.to_csv('teams_data.csv', index=False)
