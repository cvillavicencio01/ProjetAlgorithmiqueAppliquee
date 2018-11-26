from graph import *

class Greedy:
    def __init__(self, graph):
        self.graph = graph

    def execute(self):
        attackersList = self.graph.getAttackers()
        defenseList = self.graph.getDefense()
        result = []

        while len(attackersList) != 0:
            defense_max = None
            for defense in defenseList:
                if defense_max != None:
                    if len(defense.getConnections()) > len(defense_max.getConnections()):
                        defense_max = defense
                else:
                    defense_max = defense
            if len(defense_max.getConnections()) == 0:
                result
            else:
                result.append(defense_max)
                defenseList.remove(defense_max)

                for attack_element in defense_max.getConnections():
                    defense_connections = attack_element.getConnections()

                    for d in defense_connections:
                        if d in defenseList:
                            d.removeNeighbor(attack_element)

                    attack_element.removeAllNeighbors()
                    if attack_element in attackersList:
                        attackersList.remove(attack_element)
        return result
