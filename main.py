#!/usr/bin/python3
import pygame
import sys
import json

from board import *
from test import *
from greedy import *

if (len(sys.argv) < 2) :
    sys.exit("Usage: " + sys.argv[0] + " <problem.json>")

problem_path = sys.argv[1]

#read problem
with open(problem_path) as problem_file:
    problem = Problem(json.load(problem_file))

#create graph
G = Graph(problem)

#initialize greedy algorithm
greedy = Greedy(G)

#search best positions
positions = []
for v in greedy.execute():
    positions.append(v.getPosition())

#dump(save) best positions
data = {}
data['defenders'] = positions
with open('configs/solution.json', 'w') as outfile:
    json.dump(data, outfile)


#read the solution
with open('configs/solution.json') as solution_file:
    solution = Solution(json.load(solution_file))

#display result
b = Board(problem, solution)
b.run()

sys.exit()
