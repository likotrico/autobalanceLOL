from itertools import product
import numpy as np

#DEFININDO A CLASSE JOGADOR
class Player:
    def __init__(self, name, points, int):
        self.name = name
        self.points = points
        self.int = int

    def getInt(self):
        return self.int

    def getPoints(self):
        return self.points

    def getName(self):
        return self.name

#FUNÇÃO QUE RECEBE DUAS LISTAS DE OBJETOS PLAYER E VERIFICA A DIFERENÇA DA SOMA DOS PONTOS DOS OBJETOS DA LISTA
def medianDiffPlayers(blueTeam, redTeam):
    medianBlue = 0
    medianRed = 0
    for i in blueTeam:
        medianBlue += i.getPoints()
    for i in redTeam:
        medianRed += i.getPoints()
    return module(medianBlue - medianRed)

#FUNÇÃO QUE FAZ O MÓDULO DE UM NÚMERO
def module(num):
    if num >= 0:
        return num
    else:
        return num*-1

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

#CRIANDO UMA LISTA DE INTEIROS DE 1 ATÉ 10 QUE REPRESENTARÁ OS INTEIROS ASSOCIADOS AOS PLAYERS
caracteres = [1,2,3,4,5,6,7,8,9,10]
permsList = []
#USANDO A FUNÇÃO DO ITERTOOLS PARA OBTER TODOS SO ARRANJOS COM REPETIÇÃO DE 5 ESPAÇOS DE 10 ELEMENTOS DISTINTOS
genComb = product(caracteres, repeat=5) # aqui e onde tens de especificar o numero de chars que cada combinacao tenha
#COLOCANDO O RESULTADO DO ARRANJO EM UMA LISTA
for subset in genComb:
    #print(subset) # tuple retornado com uma combinacao por loop
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

#CRIANDO OS OBJETOS TIPO PLAYER PARA VERIFICAR TODAS A COMBINAÇÕES POSSÍVEIS POSTERIORMENTE
player1 = Player("likotrico", 2000.0, 1)
player2 = Player("maybe god", 1400.0, 2)
player3 = Player("slottwo", 900.0, 3)
player4 = Player("Andere", 1600, 4)
#player5 = Player("mago tiririca", 900.0, 5)
player5 = Player("paulo luy", 1400.0, 5)
player6 = Player("kskuat", 2200.0, 6)
player7 = Player("leaftime", 2800.0, 7)
player8 = Player("mary", 600.0, 8)
#player8 = Player("felipin", 1600.0, 8)
player9 = Player("marco", 500.0, 9)
player10 = Player("marx", 700.0, 10)

#CRIANDO UMA LISTA DE PLAYERS COM OS OBJETOS CRIADOS
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

#VARIÁVEL DA DIFERENÇA SETADA COMO INFINITO. COMO QUEREMOS DOIS TIMES COM A MENOR DIFERENÇA DE PONTOS,
#O VALOR INICIAL É COLOCADO COMO INFINITO PARA PEGARMOS A PRIMEIRA DIFERENÇA
mindiff = np.inf
team = []

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
    medianAux = medianDiffPlayers(blueTeam, redTeam)

    #SE A COMBINAÇÃO ATUAL RESULTOU EM UMA DIFERENÇA MENOR, ENTÃO É A COMBINAÇÃO QUE DESEJAMOS
    #SENDO ASSIM, ARMAZENAMOS A NOVA DIFERENÇA E OS TIMES DA COMBINAÇÃO.
    if medianAux < mindiff:
        #print("Entrou")
        mindiff = medianAux
        team = redTeam.copy()
        team2 = blueTeam.copy()

    redTeam.clear()
    AuxIndexList.clear()

#MOSTRAR OS TIMES RESULTANTES
if len(team) == len(team2):
    a = 0
    b = 0
    for i in range(len(team)):
        a+= team[i].points
        b+= team2[i].getPoints()
        print(f"Index:{team[i].getInt()} / Player:{team[i].getName()}\t Index:{team2[i].getInt()} / Player:{team2[i].getName()}")
    print(f"Pontos totais:\nTime 1:{a}\nTime 2:{b}")
    print(f"Diferença:{mindiff}")

else:
    print("Times com tamanhos diferentes! Um Erro aconteceu")








