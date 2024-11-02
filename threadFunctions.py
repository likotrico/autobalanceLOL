import threading
from datasetFunctions import searchPlayer

def searchLanesInfoThreads(dataset):
    allPlayers = []
    for i in range(len(dataset)):

        print(dataset.iloc[i, 0])

        player_name = dataset.at[i, 'nick']
        player_name = player_name.replace(" ", "+")
        player_tag = dataset.at[i, 'tag']

        player = player_name+"-"+player_tag
        allPlayers.append([player, i])
    
    threadArray = []
    for i in range(0, 10):
        threadArray.append(threading.Thread(target=searchPlayer,args=(dataset,allPlayers[i][0],i,)))
    
    for i in range(0, 10):
        threadArray[i].start()
    
    for i in range(0, 10):
        threadArray[i].join()

