import random
import numpy
import heapq
import string
import time
import heuristics
import graphgeneration
import traverse
from graph import Graph

def main():
	for i in range(100):
		startPoint = 0
		endPoint = 0
		while startPoint == endPoint:
			startPoint = chr(random.randint(0, 25) + ord('A')) 
			endPoint = chr(random.randint(0, 25) + ord('A'))
		mapValue = graphgeneration.randomMapGeneration()
		euclideanMap = graphgeneration.euclideanMapModify(mapValue)
		weightedGraph = graphgeneration.pruneEuclideanMap(euclideanMap)
		weightedGraphMapping = graphgeneration.euclideanMapValues(mapValue)
		unWeightedGraph = graphgeneration.createUnweightedGrapth(weightedGraph)

		graph = Graph()
		graph.edges = unWeightedGraph
		graph.weights = weightedGraphMapping

		startTime = time.time();
		previous, currentCost, aStarTimeComplexity, aStarSpaceComplexity = heuristics.aStarSearch(graph, startPoint, endPoint, 1)
		totalTime = time.time() - startTime;
		print "Astar with Euclidean Distance"
		print heuristics.reconstructPath(previous, startPoint, endPoint)
		print aStarTimeComplexity
		print aStarSpaceComplexity
		print totalTime
		startTime = time.time();
		previous, currentCost, aStarTimeComplexity, aStarSpaceComplexity = heuristics.aStarSearch(graph, startPoint, endPoint, 2)
		totalTime = time.time() - startTime;
		print "Astar with Chebyshev Distance"
		print heuristics.reconstructPath(previous, startPoint, endPoint)
		print aStarTimeComplexity
		print aStarSpaceComplexity
		print totalTime
		startTime = time.time();
		previous, greedyTimeComplexity, greedySpaceComplexity = heuristics.greedyFirstSearch(graph, startPoint, endPoint, 1)
		totalTime = time.time() - startTime;
		print "Greedy with Euclidean Distance"
		print heuristics.reconstructPath(previous, startPoint, endPoint)
		print greedyTimeComplexity
		print greedySpaceComplexity
		print totalTime
		startTime = time.time();
		previous, greedyTimeComplexity, greedySpaceComplexity = heuristics.greedyFirstSearch(graph, startPoint, endPoint, 2)
		totalTime = time.time() - startTime;
		print "Greedy with Chebyshev Distance"
		print heuristics.reconstructPath(previous, startPoint, endPoint)
		print greedyTimeComplexity
		print greedySpaceComplexity
		print totalTime


	# graph = {'A': set(['B', 'C']),
 #         'B': set(['A', 'D', 'E']),
 #         'C': set(['A', 'F']),
 #         'D': set(['B']),
 #         'E': set(['B', 'F']),
 #         'F': set(['C', 'E'])}
 	
 	# for i in range(100):
	# startPoint = 0
	# endPoint = 0
	# while startPoint == endPoint:
	# 	startPoint = chr(random.randint(0, 25) + ord('A')) 
	# 	endPoint = chr(random.randint(0, 25) + ord('A'))
				
	# mapValue = graphgeneration.randomMapGeneration()
	# euclideanMap = graphgeneration.euclideanMapModify(mapValue)
	# weightedGraph = graphgeneration.pruneEuclideanMap(euclideanMap)
	# unWeightedGraph = graphgeneration.createUnweightedSetGrapth(weightedGraph)
	# startTime = time.time();
	# breadthFirstSearch, breadthFirstTimeComplexity, breadthFirstSearchSpaceComplexity = traverse.bfs(unWeightedGraph, startPoint, endPoint)
	# totalTime = time.time() - startTime;
	# print "Breadth First Search"
	# print breadthFirstSearch
	# print breadthFirstTimeComplexity
	# print breadthFirstSearchSpaceComplexity
	# print totalTime
	# startTime = time.time();
	# depthFirstSearch, depthFirstSearchTimeComplexity, depthFirstSearchSpaceComplexity = traverse.dfs(unWeightedGraph, startPoint, endPoint)
	# totalTime = time.time() - startTime;
	# print "Depth First Search"
	# print depthFirstSearch
	# print depthFirstSearchTimeComplexity
	# print depthFirstSearchSpaceComplexity
	# print totalTime
	# startTime = time.time();
	# iterativeDeeping, iterativeDeepingTimeComplexity, iterativeDeepingSpaceComplexity = traverse.id_dfs(unWeightedGraph, startPoint, endPoint)
	# totalTime = time.time() - startTime;
	# print "Iterative Deeping"
	# print iterativeDeeping
	# print iterativeDeepingTimeComplexity
	# print iterativeDeepingSpaceComplexity
	# print totalTime


if __name__ == '__main__':
	main()
