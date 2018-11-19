from problem import *
from vertex import *

class Graph:

    def __init__(self, problem):
        self.problem = problem
        self.vertList = []
        self.numVertices = 0
        self.buildGraphForOpponents()


    def buildGraphForOpponents(self):
        self.createKicks()

    def addVertex(self,v):
        self.numVertices = self.numVertices + 1
        self.vertList.append(v)

    #def getVertex(self,n):
    #    if n in self.vertList:
    #        return self.vertList[n]
    #    else:
    #        return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t):
        f.addNeighbor(t)
        t.addNeighbor(f)

    def getVertices(self):
        return self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def createKicks(self):
        for opp_id in range(self.problem.getNbOpponents()):
            kick_dir = 0
            while kick_dir < 2 * math.pi:
                self.createKick(self.problem.getOpponent(opp_id), kick_dir)
                kick_dir += self.problem.theta_step

    def createKick(self, robot_pos, kick_dir):
        # Getting closest goal to score
        kick_end = None
        best_dist = None
        for goal in self.problem.goals:
            kick_result = goal.kickResult(robot_pos, kick_dir)
            if not kick_result is None:
                goal_dist = numpy.linalg.norm(robot_pos - kick_result)
                if best_dist == None or goal_dist < best_dist:
                    best_dist = goal_dist
                    kick_end = kick_result
        if not kick_end is None:
            vertex = Vertex("v"+str(self.numVertices), robot_pos, kick_end, self.problem.robot_radius, RobotType.Attack)
            self.addVertex(vertex)
            #print('Pi= %s, \tPf= %s' % (str(robot_pos),str(kick_end)))
