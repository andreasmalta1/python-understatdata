import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

base_url = 'https://understat.com/match/'
match = str(input("Match ID: "))
url = base_url + match

response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
scripts = soup.find_all('script')

strings = scripts[1].string

ind_start = strings.index("('") + 2
ind_end = strings.index("')")

json_data = strings[ind_start:ind_end]
json_data = json_data.encode('utf8').decode('unicode_escape')
data = json.loads(json_data)

x = []
y = []
xg = []
team = []

data_home = data['h']
data_away = data['a']

for i in range(len(data_home)):
  for key in data_home[i]:
    if key == 'X':
      x.append(data_home[i][key])
    if key == 'Y':
      y.append(data_home[i][key])
    if key == 'xG':
      xg.append(data_home[i][key])
    if key == 'h_team':
      team.append(data_home[i][key])

for i in range(len(data_away)):
  for key in data_away[i]:
    if key == 'X':
      x.append(data_away[i][key])
    if key == 'Y':
      y.append(data_away[i][key])
    if key == 'xG':
      xg.append(data_away[i][key])
    if key == 'a_team':
      team.append(data_away[i][key])

col_names = ['x', 'y', 'xg', 'team']
df = pd.DataFrame([x, y, xg, team], index=col_names)

df = df.T
print(df)