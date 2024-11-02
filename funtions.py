import numpy as np
from Player import Player
from itertools import product

def onlyPointsDiffTeams(blueteam, redteam):
  pointsBlue = 0
  pointsRed = 0
  for p in blueteam:
    pointsBlue += p.getRegularPoints()
  for p in redteam:
    pointsRed += p.getRegularPoints()
  return [abs(pointsBlue - pointsRed), pointsBlue, pointsRed]

def func(blueteam, redteam):
  pointsBlue = 0
  pointsRed = 0
  for i, p in enumerate(blueteam):
    pointsBlue += p.getLanePoints(i)+p.getPoints()

  for i, p in enumerate(redteam):
    pointsRed += p.getLanePoints(i)+p.getPoints()

  return [abs(pointsBlue - pointsRed), pointsBlue, pointsRed]

#FUNÇÃO QUE VERIFICA SE EXISTE UM ELEMENTO REPETIDO NO ELEMENTO DO ARRANJO
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

def validationTeamLane(team):
  count = 0
  for i, p in enumerate(team):
    if(p.getBanVector(i) == 0):
      count += 1
  if count == 5:
    return True
  return False

def generateAllCombinations():
    #CRIANDO UMA LISTA DE INTEIROS DE 1 ATÉ 10 QUE REPRESENTARÁ OS INTEIROS ASSOCIADOS AOS PLAYERS
    caracteres = [1,2,3,4,5,6,7,8,9,10]
    permsList = []
    #USANDO A FUNÇÃO DO ITERTOOLS PARA OBTER TODOS SO ARRANJOS COM REPETIÇÃO DE 5 ESPAÇOS DE 10 ELEMENTOS DISTINTOS
    genComb = product(caracteres, repeat=5)
    #COLOCANDO O RESULTADO DO ARRANJO EM UMA LISTA
    for subset in genComb:
        permsList.append(subset)
    #VERIFICANDO OS ELEMENTOS DO ARRANJO QUE TEM UM PELO MENOS UM DOS ELEMENTOS REPETIDOS E COLETANDO SEUS INDICES NA LISTA
    #CASO NÃO EXISTA NO MÍNIMO DOIS ELEMENTOS REPETIDOS, OU SEJA, TODOS OS ELEMENTOS SÃO DIFERENTES NO ARRANJO, PEGAMOS SEU INDICE
    indexList = []
    num = 0
    for j in range(len(permsList)):
        if haveTwice(permsList[j]):
            num+=1
        else:
            indexList.append(j) 
    #AO COLOCAR APENAS OS ELEMENTOS DO ARRANJO QUE NÃO TEM ELEMENTO REPETIDO, OBTEMOS A COMBINAÇÃO DE 5 ESPAÇOS DE 10 ELEMENTOS DISTINTOS.
    #A OPERAÇÃO É REALIZADA COLOCANDO OS INDICES COLETADOS QUE SATISFAZEM A CONDIÇÃO EM UMA NOVA LISTA
    newList = []
    for i in indexList:
        newList.append(permsList[i])
    permsList.clear()
    return newList       

def balancedByPointsOnly(players):
    newList = generateAllCombinations()
    mindiff = np.inf
    allteams = []
    
    for comb in newList:
      blueTeam = players.copy()
      redTeam = []
      AuxIndexList = []
    
      for integer in comb:
              for element in range(len(players)):
                  if players[element].getInt() == integer:
                      AuxIndexList.append(element)
      
      for i in AuxIndexList:
              redTeam.append(blueTeam[i])
              
      for i in redTeam:
              for j in blueTeam:
                  if i.getInt() == j.getInt():
                      blueTeam.remove(j)
      
      test = onlyPointsDiffTeams(blueTeam, redTeam)
      medianAux = test[0]
      
      if medianAux < mindiff:
        mindiff = medianAux
        allteams.clear()
        allteams.append([redTeam.copy(), blueTeam.copy(), medianAux])  
      elif medianAux == mindiff:
        allteams.append([redTeam.copy(), blueTeam.copy(), medianAux])
        
      redTeam.clear()
      AuxIndexList.clear()
      
    return allteams

def balanceByPositions(matchsArray):
  mindiff = np.inf
  bestTeams = []
  for match in matchsArray:
    redTeam = match[0]
    blueTeam = match[1]
    result = func(blueTeam, redTeam)
    medianAux = result[0]
    if(medianAux < mindiff):
      mindiff = medianAux
      bestTeams.clear()
      bestTeams.append([redTeam.copy(), blueTeam.copy(), medianAux])
  
  return bestTeams
    
def genAll(players):
    #VARIÁVEL DA DIFERENÇA SETADA COMO INFINITO. COMO QUEREMOS DOIS TIMES COM A MENOR DIFERENÇA DE PONTOS,
    #O VALOR INICIAL É COLOCADO COMO INFINITO PARA PEGARMOS A PRIMEIRA DIFERENÇA
    newList = generateAllCombinations()
    mindiff = np.inf
    team = []
    allteams = []
    teamsWithBanLanes = []
    contador = 0

    for comb in newList:
        #AQUI VAMO TER UMA LISTA QUE ARMAZENARÁ A LISTA PLAYER, NO CASO A BLUETEAM. DEPOIS, VERIFICANDO OS ELEMENTOS DA COMBINAÇÃO,
        #VAMOS
        blueTeam = players.copy()
        redTeam = []
        AuxIndexList = []
        #COLETANDO OS INDICES DA LISTA CUJO INTEIRO DO PLAYER CONDIZ COM OS NUMERO PRESENTE NA COMBINAÇÃO
        for integer in comb:
            for element in range(len(players)):
                if players[element].getInt() == integer:
                    AuxIndexList.append(element)
        #ADICIONANDO OS PLAYERS QUE TEM OS INTEIROS CONDIZENTES COM O ELEMENTO DA COMBINAÇÃO ATUAL
        for i in AuxIndexList:
            redTeam.append(blueTeam[i])

        #REMOVENDO OS ELEMENTOS QUE ESTÃO NO REDTEAM DA LISTA DO BLUETEAM, QUE INICIALMENTE POSSUI TODOS OS PLAYERS
        for i in redTeam:
            for j in blueTeam:
                if i.getInt() == j.getInt():
                    blueTeam.remove(j)

        #REALIZANDO A DIFERENÇA DA SOMA DOS PONTOS DOS TIMES RESULTANTES DA COMBINAÇÃO VERIFICADA
        test = func(blueTeam, redTeam)
        medianAux = test[0]
        bluesum = test[1]
        redsum = test[2]

        if medianAux <= 0.001:
            allteams.append([redTeam.copy(), blueTeam.copy(), medianAux])
        #VERIFICAR SE AS EQUIPES SATISFAZEM AS CONDIÇÕES DAS LANES BANIDAR PELOS PLAYERS
        if(validationTeamLane(blueTeam) and validationTeamLane(redTeam)):
            teamsWithBanLanes.append([redTeam.copy(), blueTeam.copy(), medianAux])

        redTeam.clear()
        AuxIndexList.clear()
        
    return allteams

def sortTeams(allTeams):
  result = []
  for i in allTeams:
    if len(result) == 0:
      result.append(i)
    else:
      var = False
      for j in range(len(result)):
        if i[2] <= result[j][2]:
          result.insert(j, i)
          var = True
          break
      if var == False:
        result.append(i)
  return result