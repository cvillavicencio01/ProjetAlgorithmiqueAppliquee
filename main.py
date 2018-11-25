#!/usr/bin/python3
import pygame
import sys
import json

from board import *
from test import *
from greedy import *

if (len(sys.argv) < 3) :
    sys.exit("Usage: " + sys.argv[0] + " <problem.json> <solution.json>")

problem_path = sys.argv[1]
solution_path = sys.argv[2]

with open(problem_path) as problem_file:
    problem = Problem(json.load(problem_file))

with open(solution_path) as solution_file:
    solution = Solution(json.load(solution_file))

G = Graph(problem)

greedy = Greedy(G)
for e in greedy.execute():
    print(e.getId())


#b = Board(problem, solution)
#b.run()

sys.exit()
