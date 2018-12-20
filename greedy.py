from graph import *

class Greedy:
    def __init__(self, graph):
        self.graph = graph

    def execute(self):
        attackers_list = self.graph.getAttackers()
        defense_list = self.graph.getDefense()

        solution = []

        for a in attackers_list:
            if len(a.getConnections()) == 0 :
                return solution

        while len(attackers_list) != 0:
            defender_max = None
            for defender in defense_list:
                if defender_max != None:
                    if len(defender.getConnections()) > len(defender_max.getConnections()):
                        defender_max = defender
                else:
                    defender_max = defender
            if len(defender_max.getConnections()) == 0:
                return solution
            else:
                solution.append(defender_max)
                defense_list.remove(defender_max)

                for attack_element in defender_max.getConnections():
                    defense_connections = attack_element.getConnections()

                    for d in defense_connections:
                        if d in defense_list:
                            d.removeNeighbor(attack_element)

                    attack_element.removeAllNeighbors()

                    if attack_element in attackers_list:
                        attackers_list.remove(attack_element)
        return solution
