import numpy as np
import requests
from bs4 import BeautifulSoup

def normalizeLP(dataset):
  max = np.inf * -1
  min = np.inf
  for i in dataset['points']:
    if i > max:
      max = i
    if i < min:
      min = i
  for i in range(len(dataset['points'])):
    dataset.at[i, 'normalized'] = (dataset.at[i, 'points'] - min)/(max - min)
    
    
def searchPlayer(dataset, player, i):
    lanes = ['top', 'jungle', 'middle', 'adc', 'support']
    lane_ref = ['top', 'jg', 'mid', 'adc', 'sup']
    player_info = []
    total_matchs = 0
    
    for j in range(len(lanes)):
      url = 'https://www.leagueofgraphs.com/pt/summoner/champions/br/'+player+'/'+lanes[j]
      headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
      site = requests.get(url, headers=headers)
      soup = BeautifulSoup(site.content, 'html.parser')
      partidas = soup.find_all('div', class_='pie-chart small')
      aux = []
      if len(partidas) != 0:
        num_matchs = float(partidas[2].get_text().strip())
        total_matchs += num_matchs
        string_winrate = partidas[3].get_text().strip()
        string_winrate = string_winrate.replace("%", "")
        winrate = float(string_winrate)/100
        aux.append(num_matchs)
        aux.append(winrate)
      else:
        aux.append(0.0)
        aux.append(0.0)

      player_info.append(aux.copy())
      aux.clear()

    for j in range(len(lanes)):
      if total_matchs != 0:
        dataset.at[i, lane_ref[j]] = (player_info[j][0]*player_info[j][1])/total_matchs
      else:
        dataset.at[i, lane_ref[j]] = 0
        
"""def searchLanesInfo(dataset):
  lanes = ['top', 'jungle', 'middle', 'adc', 'support']
  lane_ref = ['top', 'jg', 'mid', 'adc', 'sup']
  for i in range(len(dataset)):

    print(dataset.iloc[i, 0])


    player_name = dataset.at[i, 'nick']
    player_name = player_name.replace(" ", "+")
    player_tag = dataset.at[i, 'tag']

    player = player_name+"-"+player_tag
    player_info = []

    total_matchs = 0
    for j in range(len(lanes)):

      #print(lanes[j])

      url = 'https://www.leagueofgraphs.com/pt/summoner/champions/br/'+player+'/'+lanes[j]
      headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
      site = requests.get(url, headers=headers)
      soup = BeautifulSoup(site.content, 'html.parser')
      partidas = soup.find_all('div', class_='pie-chart small')

      aux = []
      #print(partidas)
      if len(partidas) != 0:
        num_matchs = float(partidas[2].get_text().strip())
        total_matchs += num_matchs
        string_winrate = partidas[3].get_text().strip()
        string_winrate = string_winrate.replace("%", "")
        winrate = float(string_winrate)/100
        #print(f"num matchs:{num_matchs}")
        #print(f"winrate:{winrate}")
        aux.append(num_matchs)
        aux.append(winrate)
      else:
        aux.append(0.0)
        aux.append(0.0)

      player_info.append(aux.copy())
      aux.clear()
    #print(f"total matchs:{total_matchs}")
    #print(player_info)

    for j in range(len(lanes)):
      #print("a")
      #print((player_info[j][0]*player_info[j][1])/total_matchs)
      if total_matchs != 0:
        dataset.at[i, lane_ref[j]] = (player_info[j][0]*player_info[j][1])/total_matchs
      else:
        dataset.at[i, lane_ref[j]] = 0"""