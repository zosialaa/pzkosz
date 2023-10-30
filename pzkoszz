import requests
import pandas as pd
from bs4 import BeautifulSoup
import openpyxl  # import to excel
from tabulate import tabulate  # format



r = requests.get("https://rozgrywki.pzkosz.pl/liga/4/tabela.html")


soup = BeautifulSoup(r.text, "html.parser")


table = soup.find("table", class_="stattype splitTable tabela").find('tbody').find_all('tr')

table_data = []

for row in table:
    dic = {}

    row_data = row.find_all('td')
    dic['place'] = row_data[0].text
    dic['team'] = row_data[1].text
    dic['matches'] = row_data[2].text
    dic['points'] = row_data[3].text
    dic['win-lose'] = row_data[4].text
    dic['home'] = row_data[5].text
    dic['away'] = row_data[6].text
    dic['p_scored-p_lost'] = row_data[7].text
    dic['difference'] = row_data[8].text
    dic['win/matches'] = row_data[9].text
    table_data.append(dic)


#for key, value in dic.items():
 #   table.append([key, value])

headers = table_data[0].keys()
print(tabulate(table_data, headers="keys", tablefmt="grid"))


df = pd.DataFrame(table_data)
df.to_excel('teams_data.xlsx', index=False)
df.to_csv('teams_data.csv', index=False)



