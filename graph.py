from problem import *
from vertex import *

class Graph:

    def __init__(self, problem):
        self.problem = problem
        self.vertList = []
        self.numVertices = 0
        self.createAttackers()
        self.createDefense()
        self.createEdges()

    def addVertex(self,v):
        self.numVertices = self.numVertices + 1
        self.vertList.append(v)

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t):
        f.addNeighbor(t)
        t.addNeighbor(f)

    def getVertices(self):
        return self.vertList

    def getAttackers(self):
        return list(filter(lambda x: x.getType() == RobotType.Attack, self.getVertices()))

    def getDefense(self):
        return list(filter(lambda x: x.getType() == RobotType.Defense, self.getVertices()))

    def __iter__(self):
        return iter(self.vertList.values())

    def createAttackers(self):
        for opp_id in range(self.problem.getNbOpponents()):
            kick_dir = 0
            while kick_dir < 2 * math.pi:
                self.createAttacker(self.problem.getOpponent(opp_id), kick_dir)
                kick_dir += self.problem.theta_step

    def createAttacker(self, robot_pos, kick_dir):
        kick_end = self.getKickEnd(robot_pos, kick_dir)
        if not kick_end is None:
            vertex = Vertex("Attack : %s, direction : %s"%(str(robot_pos),str(kick_dir)), robot_pos, kick_dir, self.problem.robot_radius, RobotType.Attack)
            self.addVertex(vertex)

    def getKickEnd(self, robot_pos, kick_dir):
        kick_end = None
        best_dist = None
        for goal in self.problem.goals:
            kick_result = goal.kickResult(robot_pos, kick_dir)
            if not kick_result is None:
                goal_dist = numpy.linalg.norm(robot_pos - kick_result)
                if best_dist == None or goal_dist < best_dist:
                    best_dist = goal_dist
                    kick_end = kick_result
        return kick_end

    def createEdges(self):
        attack = list(filter(lambda x: x.getType() == RobotType.Attack, self.getVertices()))
        defense = list(filter(lambda x: x.getType() == RobotType.Defense, self.getVertices()))

        for d in defense:
            for a in attack:
                collide_point = segmentCircleIntersection(a.getPosition(), self.getKickEnd(a.getPosition(),a.getKickDirection()), d.getPosition(), d.getRadius())
                if not collide_point is None:
                    self.addEdge(a,d)

    def createDefense(self):
        x_start = self.problem.field_limits[0][0]
        x_end = self.problem.field_limits[0][1]
        y_start = self.problem.field_limits[1][0]
        y_end = self.problem.field_limits[1][1]

        for x in numpy.arange(x_start, x_end, self.problem.pos_step):
            for y in numpy.arange(y_start, y_end, self.problem.pos_step):
                v = Vertex("Defense : %s"%(str([x,y])),[x,y], None, self.problem.robot_radius, RobotType.Defense)
                self.addVertex(v)
