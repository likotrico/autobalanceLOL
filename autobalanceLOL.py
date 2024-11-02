import pandas as pd

from Player import Player
from datasetFunctions import normalizeLP
from funtions import genAll, sortTeams, balancedByPointsOnly, balanceByPositions
from printFunctions import showTeams
from threadFunctions import searchLanesInfoThreads

#IMPORTANDO ARQUIVO .CSV COM OS INFORMAÇÕES DOS JOGADORES
input_file = open("inputFile.csv", 'r')
#CRIANDO UM DATASET PANDAS COM O ARQUIVO .CSV DE ENTRADA
dataset = pd.read_csv(input_file)
normalizeLP(dataset)
searchLanesInfoThreads(dataset)
print(dataset)
players = []
for i in range(len(dataset["nick"])):
  players.append(Player(dataset.iloc[i, 0], dataset.iloc[i, 9], dataset.iloc[i, 3], dataset.iloc[i, 2], [dataset.iloc[i, 4], dataset.iloc[i, 5], dataset.iloc[i, 6], dataset.iloc[i, 7], dataset.iloc[i, 8]] ,dataset.iloc[i, 10], dataset.iloc[i, 11], dataset.iloc[i, 12], dataset.iloc[i, 13] ,dataset.iloc[i, 14]))
bestMatchByPointsOnly = balancedByPointsOnly(players)
bestMatchByLane = balanceByPositions(bestMatchByPointsOnly)
showTeams(bestMatchByLane)