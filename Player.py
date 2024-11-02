#DEFININDO A CLASSE JOGADOR
class Player:
    def __init__(self, name, points, regularPoints, int, banvector,*lane_points): #NEW
        self.name = name
        self.points = points
        self.regularPoints = regularPoints
        self.int = int
        self.lane_points = lane_points
        self.banvector = banvector

    def getInt(self):
        return self.int

    def getPoints(self):
        return self.points

    def getName(self):
        return self.name
    
    def getRegularPoints(self):
        return self.regularPoints

    def getLanePoints(self, index):
      return self.lane_points[index]

    #NEW
    def getBanVector(self, index):
      return self.banvector[index]