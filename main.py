#!/usr/bin/python3
import pygame
import sys
import json
import time
import argparse

from board import *
from greedy import *
from brute_force import *



parser = argparse.ArgumentParser(description='Robocup (Projet d\'Algorithmique Appliquée)')

parser.add_argument('-g','--graph', action='store_true', help='display graphical result with players', default = True )
parser.add_argument('-t', '--time', action="store_true", help='shows the algorithm time (without graphical view)', default=False )
parser.add_argument('-a', '--algo', default="greedy", choices=['greedy', 'brute'], help="search algorithm")
parser.add_argument('filename', help="Json file problem")

args = parser.parse_args()


#read problem
with open(args.filename) as problem_file:
    problem = Problem(json.load(problem_file))

#create graph
if args.time:
    start_time = time.time()
G = Graph(problem)
if args.time:
    print("--Graph construction time: %s seconds --" % (time.time() - start_time))


#initialize algorithm
algo = None
if args.algo == 'greedy':
    algo = Greedy(G)
else:
    algo = BruteForce(G)


#search best positions
positions = []

if args.time:
    start_time = time.time()

for v in algo.execute():
    positions.append(v.getPosition())

if args.time:
    print("--Algorithm time: %s seconds --" % (time.time() - start_time))


#dump(save) best positions
data = {}
data['defenders'] = positions
with open('configs/solution.json', 'w') as outfile:
    json.dump(data, outfile)

#display result
if not args.time:
    #read the solution
    with open('configs/solution.json') as solution_file:
        solution = Solution(json.load(solution_file))
    b = Board(problem, solution)
    b.run()

sys.exit()
