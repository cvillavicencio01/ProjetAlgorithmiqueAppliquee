
from RobotType import *

class Vertex:
    def __init__(self, id, pos, kick_dir, radius, type):
        self.id = id
        self.robot_pos = pos
        self.kick_dir = kick_dir
        self.radius = radius
        self.type = type
        self.connectedTo = []

    def addNeighbor(self,v):
        self.connectedTo.append(v)

    def removeNeighbor(self,v):
        if v in self.connectedTo:
            self.connectedTo.remove(v)

    def removeAllNeighbors(self):
        self.connectedTo.clear()

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def getId(self):
        return self.id

    def getPosition(self):
        return self.robot_pos

    def getKickDirection(self):
        return self.kick_dir

    def getRadius(self):
        return self.radius
