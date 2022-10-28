import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def get_data():
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
	return json.loads(json_data)


def get_xg(data):

	x, y, xg, team, minute = [], [], [], [], []

	data_home = data['h']
	data_away = data['a']

	for shot_event in data_home:
		x.append(shot_event['X'])
		y.append(shot_event['Y'])
		xg.append(shot_event['xG'])
		team.append(shot_event['h_team'])
		minute.append(shot_event['minute'])

	for shot_event in data_away:
		x.append(shot_event['X'])
		y.append(shot_event['Y'])
		xg.append(shot_event['xG'])
		team.append(shot_event['a_team'])
		minute.append(shot_event['minute'])

	col_names = ['x', 'y', 'xg', 'team', 'minute']
	df = pd.DataFrame([x, y, xg, team, minute], index=col_names)

	return df.T


def get_flow_chart(xg_df):
	pass


def main():
	data = get_data()
	xg_df = get_xg(data)
	print(xg_df)
	get_flow_chart(xg_df)


main()