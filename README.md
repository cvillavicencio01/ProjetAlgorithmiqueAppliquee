# Projet d'Algorithmique Appliquée
## Master 2 Informatique - Université de Bordeaux

Ce projet a comme contexte la compétition mondiale de robotique RoboCup et plus particulièrement la ligue SSL. Dans cettes compétition, plusieurs robots à roues se déplacent rapidement et disputent un match de football robotique.

Dans le cadre de ce projet, l'objectif sera de traiter le problème de la défense. Soit: comment placer les défenseurs pour éviter que les attaquants aient un angle de tir? Le problème sera abordé avec différents niveaux de simplifications et sera modélisé comme un problème de graphe.


#Usage: 
main.py *[-h] [-g] [-t] [-a {greedy,brute}]* **filename**

positional arguments:

	filename              Json file problem

optional arguments:
  
 	-h, --help            show this help message and exit
 	-g, --graph           display a graphical result
	-t, --time            show the algorithm time (without the graphical view)
  	-a {greedy,brute}, --algo {greedy,brute}       search algorithm