#!/usr/bin/python3
import pygame
import sys
import json

from board import *

if (len(sys.argv) < 3) :
    sys.exit("Usage: " + sys.argv[0] + " <problem.json> <solution.json>")

problem_path = sys.argv[1]
solution_path = sys.argv[2]

with open(problem_path) as problem_file:
    problem = Problem(json.load(problem_file))

with open(solution_path) as solution_file:
    solution = Solution(json.load(solution_file))


graph = Graph()
for opp_id in range(problem.getNbOpponents()):
    v = Vertex("opp{}".format(opp_id), problem.getOpponent(opp_id), RobotType.Attack)
    graph.addVertex(v)

v = Vertex("test",[0,0],RobotType.Defense)
graph.addVertex(v)


"""for def_id in range(solution.getNbDefenders()):
    v = Vertex("def{}".format(def_id), solution.getDefender(def_id), RobotType.Defense)
    graph.addVertex(v)"""
"""graph.addEdge(graph.getVertices()[0], graph.getVertices()[3])
graph.addEdge(graph.getVertices()[1], graph.getVertices()[4])
graph.addEdge(graph.getVertices()[2], graph.getVertices()[5])"""

opponnents = list(filter(lambda x: x.id[:3] == "opp", graph.getVertices()))

if graph.existDominant(opponnents):
    print("On a dominant")
else:
    print("On na pas dominant")

#for o in opponnents:
#    if len(o.connectedTo) == 0:
#        print("On nas pas dominant")
#        break
#    else:
#        print("On as dominant")

#print(opponnents)
#print (graph.getVertices()[1])

b = Board(problem, solution)
b.run()
sys.exit()
