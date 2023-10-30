import requests
import pandas as pd
from bs4 import BeautifulSoup
import openpyxl  # import to excel
from tabulate import tabulate  # format

url = "https://rozgrywki.pzkosz.pl/liga/4/statystyki/druzynowe.html"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

table = soup.find("table", class_="statystyki druzynowe stattype splitTable").find('tbody').find_all('tr')

table_data = []

#print(table)

for row in table:
    dic = {}

    row_data = row.find_all('td')
    dic['team'] = row_data[0].text
    dic['m'] = row_data[1].text
    dic['points'] = row_data[2].text
    dic['2/c'] = row_data[3].text
    dic['2/w'] = row_data[4].text
    dic['[2/%]'] = row_data[5].text
    dic['3/c'] = row_data[6].text
    dic['3/w'] = row_data[7].text
    dic['3/%'] = row_data[8].text
    dic['game/c'] = row_data[9].text
    dic['game/w'] = row_data[10].text
    dic['[game/%]'] = row_data[11].text
    dic['1/c'] = row_data[12].text
    dic['1/w'] = row_data[13].text
    dic['1/%'] = row_data[14].text
    dic['zb/a'] = row_data[15].text
    dic['zb/0'] = row_data[16].text
    dic['zb/s'] = row_data[17].text
    dic['a'] = row_data[18].text
    dic['f'] = row_data[19].text
    dic['[fw]'] = row_data[20].text
    dic['s'] = row_data[21].text
    dic['p'] = row_data[22].text
    dic['b'] = row_data[23].text
    dic['bo'] = row_data[24].text
    dic['eval'] = row_data[25].text

   
    table_data.append(dic)
#print(table_data)

# for key, value in dic.items():
 #   table.append([key, value])

headers = table_data[0].keys()
print(tabulate(table_data, headers="keys", tablefmt="grid"))


df = pd.DataFrame(table_data)
df.to_excel('teams_data.xlsx', index=False)
df.to_csv('teams_data.csv', index=False)
