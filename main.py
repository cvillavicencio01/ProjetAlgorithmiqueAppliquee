#!/usr/bin/python3
import pygame
import sys
import json

from board import *
from test import *

if (len(sys.argv) < 3) :
    sys.exit("Usage: " + sys.argv[0] + " <problem.json> <solution.json>")

problem_path = sys.argv[1]
solution_path = sys.argv[2]

with open(problem_path) as problem_file:
    problem = Problem(json.load(problem_file))

with open(solution_path) as solution_file:
    solution = Solution(json.load(solution_file))

G = Graph(problem)


#for l in range(-4.5,4.5,0.2):
#    for h in range (-3,3,0.2):
#        print(l,h)

#for vertex in G.getVertices():
#    print('Pi= %s, \tPf= %s' % (str(vertex.getPosition()),str(vertex.getKickEnd())))

b = Board(problem, solution)
b.run()



#G = Graph(problem)
#print(G.getVertices())

#for vertex in G.getVertices():
#    print(vertex.getPosition())

sys.exit()
