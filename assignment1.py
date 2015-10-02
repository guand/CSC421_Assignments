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
	# for i in range(100):
	# 	startPoint = 0
	# 	endPoint = 0
	# 	while startPoint == endPoint:
	# 		startPoint = chr(random.randint(0, 25) + ord('A')) 
	# 		endPoint = chr(random.randint(0, 25) + ord('A'))
	# 	mapValue = randomMapGeneration()
	# 	euclideanMap = euclideanMapModify(mapValue)
	# 	weightedGraph = pruneEuclideanMap(euclideanMap)
	# 	weightedGraphMapping = euclideanMapValues(mapValue)
	# 	unWeightedGraph = createUnweightedGrapth(weightedGraph)

	# 	graph = Graph()
	# 	graph.edges = unWeightedGraph
	# 	graph.weights = weightedGraphMapping

	# 	previous, currentCost = heuristics.aStarSearch(graph, startPoint, endPoint, 1)
	# 	print heuristics.reconstructPath(previous, startPoint, endPoint)
	# 	previous, currentCost = heuristics.aStarSearch(graph, startPoint, endPoint, 2)
	# 	print heuristics.reconstructPath(previous, startPoint, endPoint)
	# 	previous = heuristics.greedyFirstSearch(graph, startPoint, endPoint, 1)
	# 	print heuristics.reconstructPath(previous, startPoint, endPoint)
	# 	previous = heuristics.greedyFirstSearch(graph, startPoint, endPoint, 2)
	# 	print heuristics.reconstructPath(previous, startPoint, endPoint)


	# graph = {'A': set(['B', 'C']),
 #         'B': set(['A', 'D', 'E']),
 #         'C': set(['A', 'F']),
 #         'D': set(['B']),
 #         'E': set(['B', 'F']),
 #         'F': set(['C', 'E'])}
 	
 	# for i in range(100):
	startPoint = 0
	endPoint = 0
	while startPoint == endPoint:
		startPoint = chr(random.randint(0, 25) + ord('A')) 
		endPoint = chr(random.randint(0, 25) + ord('A'))
				
	mapValue = graphgeneration.randomMapGeneration()
	euclideanMap = graphgeneration.euclideanMapModify(mapValue)
	weightedGraph = graphgeneration.pruneEuclideanMap(euclideanMap)
	unWeightedGraph = graphgeneration.createUnweightedSetGrapth(weightedGraph)
	startTime = time.time();
	breadthFirstSearch, breadthFirstTimeComplexity = traverse.bfs(unWeightedGraph, startPoint, endPoint)
	totalTime = time.time() - startTime;
	print "Breadth First Search"
	print breadthFirstSearch
	print breadthFirstTimeComplexity
	print totalTime
	startTime = time.time();
	depthFirstSearch, depthFirstSearchTimeComplexity = traverse.dfs(unWeightedGraph, startPoint, endPoint)
	totalTime = time.time() - startTime;
	print "Depth First Search"
	print depthFirstSearch
	print depthFirstSearchTimeComplexity
	print totalTime
	startTime = time.time();
	iterativeDeeping, iterativeDeepingTimeComplexity = traverse.id_dfs(unWeightedGraph, startPoint, endPoint)
	totalTime = time.time() - startTime;
	print "Iterative Deeping"
	print iterativeDeeping
	print iterativeDeepingTimeComplexity
	print totalTime



if __name__ == '__main__':
	main()
