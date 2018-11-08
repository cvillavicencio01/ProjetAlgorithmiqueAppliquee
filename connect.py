import numpy
import pygame

from problem import *
from solution import *
from graph import *

class Connect :
    def __init__(self, problem, solution,graph):
        self.problem = problem
        self.solution = solution
        self.graph = graph

    def drawKickRay(self, robot_pos, kick_dir, pos[]):
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
            # Checking if kick is intercepted by one of the opponent and which one is the first
            intercepted = False
            for def_id in range(self.solution.getNbDefenders()):
                defender = self.solution.getDefender(def_id)
                collide_point = segmentCircleIntersection(robot_pos, kick_end, defender, self.problem.robot_radius)
                if collide_point is None:
                    v = Vertex("test",[0,0],RobotType.Defense)
                    graph.addVertex(v)
                    drawKickRay(self, robot_pos, kick_dir)
                if not collide_point is None:
                    kick_end = collide_point
                    intercepted = True




    def drawKickRays(self):
        for opp_id in range(self.problem.getNbOpponents()):
            kick_dir = 0
            while kick_dir < 2 * math.pi:
                self.drawKickRay(screen, self.problem.getOpponent(opp_id), kick_dir)
                kick_dir += self.problem.theta_step
