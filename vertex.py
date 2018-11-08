
from RobotType import *

class Vertex:
    def __init__(self,key,pos, type):
        self.id = key
        self.robot_pos = pos
        self.type = type
        self.connectedTo = []

    def addNeighbor(self,v):
        self.connectedTo.append(v)

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo()

    def getRobotPosition(self):
        return self.robot_pos

    def setType(self, type):
        self.type = type

    def getId(self, ):
        return self.id