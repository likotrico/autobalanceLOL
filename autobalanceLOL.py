from itertools import product
import numpy as np

class Player:
    def __init__(self, name, points, int):
        self.name = name
        self.points = points
        self.int = int

    def getInt(self):
        return self.int

    def getPoints(self):
        return self.points

def medianDiffPlayers(blueTeam, redTeam):
    medianBlue = 0
    medianRed = 0
    for i in blueTeam:
        medianBlue += i.getPoints()
        #print(i.getPoints())
    #medianBlue = medianBlue/5
    for i in redTeam:
        medianRed += i.getPoints()
        #print(i.getPoints())
    #medianRed = medianRed/5
    #print(f"medianBlue:{medianBlue}")
    #print(f"medianRed:{medianRed}")
    return module(medianBlue - medianRed)

def module(num):
    if num >= 0:
        return num
    else:
        return num*-1

def haveTwice(lista):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    for element in lista:
        #print(element)
        #print(f"teste: {element == 10}")
        if element == 1:
            count1 = count1 + 1
        if element == 2:
            count2 = count2 + 1
        if element == 3:
            count3 = count3 + 1
        if element == 4:
            count4 = count4 + 1
        if element == 5:
            count5 = count5 + 1
        if element == 6:
            count6 = count6 + 1
        if element == 7:
            count7 = count7 + 1
        if element == 8:
            count8 = count8 + 1
        if element == 9:
            count9 = count9 + 1
        if element == 10:
            #print("entrou")
            count10 = count10 + 1
    #print(f"count10: {count10}")
    if count1 >= 2 or count2 >= 2 or count3 >= 2 or count4 >= 2 or count5 >= 2 or count6 >= 2 or count7 >= 2 or count8 >= 2 or count9 >= 2 or count10 >= 2:
        return True
    return False

caracteres = [1,2,3,4,5,6,7,8,9,10]
permsList = []
genComb = product(caracteres, repeat=5) # aqui e onde tens de especificar o numero de chars que cada combinacao tenha
for subset in genComb:
    #print(subset) # tuple retornado com uma combinacao por loop
    permsList.append(subset)



indexList = []
num = 0
for j in range(len(permsList)-1):
    if haveTwice(permsList[j]):
        num+=1
    else:
        indexList.append(j)

#print(indexList)
#print(f"TAMANHO {len(indexList)}")
#print(permsList[98765])



newList = []
for i in indexList:
    newList.append(permsList[i])
#print(newList)

player1 = Player("mary", 500.0, 1)
player2 = Player("slottwo", 700.0, 2)
player3 = Player("icaro", 900.0, 3)
player4 = Player("iago", 1200, 4)
#player5 = Player("luy", 1200.0, 5)
player5 = Player("mateus", 2200.0, 5)
player6 = Player("breno", 1300.0, 6)
player7 = Player("simoes", 1500.0, 7)
player8 = Player("felipin", 1600.0, 8)
player9 = Player("likotrico", 2000.0, 9)
player10 = Player("leaftime", 2800.0, 10)


players = []
players.append(player1)
players.append(player2)
players.append(player3)
players.append(player4)
players.append(player5)
players.append(player6)
players.append(player7)
players.append(player8)
players.append(player9)
players.append(player10)
#for i in range(1, 11):
#    players.append(Player(str(i), 10, i))

mindiff = np.inf
team = []

for comb in newList:
    #print(comb)
    blueTeam = players.copy()
    redTeam = []
    AuxIndexList = []
    for integer in comb:
        for element in range(len(players)-1):
            if players[element].getInt() == integer:
                AuxIndexList.append(element)

    for i in AuxIndexList:
        redTeam.append(blueTeam[i])
    for i in redTeam:
        for j in blueTeam:
            if i.getInt() == j.getInt():
                blueTeam.remove(j)

    medianAux = medianDiffPlayers(blueTeam, redTeam)
    #print(medianAux)
    if medianAux < mindiff:
        print("Entrou")
        mindiff = medianAux
        team = redTeam.copy()

    redTeam.clear()
    AuxIndexList.clear()
for i in team:
    print(i.getInt())












