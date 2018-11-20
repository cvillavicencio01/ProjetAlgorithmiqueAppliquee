from problem import *
from vertex import *

class Graph:

    def __init__(self, problem):
        self.problem = problem
        self.vertList = []
        self.numVertices = 0
        self.buildGraphForOpponents()
        self.createDefense()
        self.createEdges()


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
            vertex = Vertex("%s [%s], [%s]"%(str(self.numVertices),str(robot_pos),str(kick_end)), robot_pos, kick_end, self.problem.robot_radius, RobotType.Attack)
            self.addVertex(vertex)
            #print('Pi= %s, \tPf= %s' % (str(robot_pos),str(kick_end)))

    def createDefense(self):
        x = -self.problem.getFieldWidth()/2
        y = -self.problem.getFieldHeight()/2

        while x<self.problem.getFieldWidth()/2-0.2:
            x+=0.2
            while y<self.problem.getFieldHeight()/2-0.2:
                y+=0.2
                v = Vertex(str([round(x,1),round(y,1)]), [round(x,1),round(y,1)], [0,0], self.problem.robot_radius, RobotType.Defense)
                self.addVertex(v)
                #print(round(x,1),round(y,1))
            y=-self.problem.getFieldHeight()/2

    def createEdges(self):
        attack = list(filter(lambda x: x.getType() == RobotType.Attack, self.getVertices()))
        defense = list(filter(lambda x: x.getType() == RobotType.Defense, self.getVertices()))

        for d in defense:
            for a in attack:
                collide_point = segmentCircleIntersection(a.getPosition(), a.getKickEnd(), d.getPosition(), self.problem.robot_radius)
                if not collide_point is None:
                    self.addEdge(a,d)

        for a in attack:
            print(a)
