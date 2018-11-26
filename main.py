#!/usr/bin/python3
import pygame
import sys
import json
import time

from board import *
from test import *
from greedy import *

if (len(sys.argv) < 3) :
    sys.exit("Usage: " + sys.argv[0] + " <problem.json> <mode>")

start_time = time.time()

problem_path = sys.argv[1]
mode = sys.argv[2]

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


#display result
if mode=="-g":
    #read the solution
    with open('configs/solution.json') as solution_file:
        solution = Solution(json.load(solution_file))
    b = Board(problem, solution)
    b.run()

if mode=="-p":
    print("-- %s seconds --" % (time.time() - start_time))

sys.exit()
