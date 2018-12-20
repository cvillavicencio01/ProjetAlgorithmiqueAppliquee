from RobotType import *

class BruteForce:
    def __init__(self, graph):
        self.graph = graph
        self.solutions = []

    def execute(self):
        attackers = list(filter(lambda x: x.getType() == RobotType.Attack, self.graph.getVertices()))
        attackers_dict = dict()

        for a in attackers:
            if len(a.getConnections()) == 0 :
                return []

        for a in attackers:
            attackers_dict[a] = list(a.getConnections())

        first_solution = self.extractSolution(attackers_dict)
        self.solutions.append(first_solution)

        for defender in first_solution:
            self.searchSolution(defender, attackers_dict)

        return self.searchMinimalSolution()


    def searchMinimalSolution(self):
        final_solution = None

        for solution in self.solutions:
            if final_solution == None:
                final_solution = solution
            else:
                if len(final_solution) > len(solution):
                    final_solution = solution
        return final_solution

    def searchSolution(self, defender, attackers_dict):
        attackers_copy = dict(attackers_dict)

        for attacker, defenders_list in attackers_copy.items():
            if defender in defenders_list:
                attackers_copy[attacker] = list(defenders_list)
                attackers_copy[attacker].remove(defender)

        if self.containsValidSolution(attackers_copy):
            new_solution = self.extractSolution(attackers_copy)
            if self.isInSolutions(new_solution):
                return

            self.solutions.append(new_solution)
            for new_defender in new_solution:
                self.searchSolution(new_defender, attackers_copy)

    def isInSolutions(self, solution):
        for sol in self.solutions:
            if self.isSameSolution(solution,sol):
                return True
        return False

    def isSameSolution(self, sol1, sol2):
        if len(sol1) == len(sol2):
            return sol1 == sol2
        else:
            return False

    def extractSolution(self, attackers):
        sol = set()
        for attacker, defenders in attackers.items():
            for d in defenders:
                sol.add(d)
        return sol

    def containsValidSolution(self, attackers):
        for attacker, defenders in attackers.items():
            if len(defenders) == 0:
                return False
        return True
