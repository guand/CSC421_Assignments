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
# Heuristic Bench marks
	misses = 0
 	incrementor = 0
 	aStarEuclideanList = []
 	aStarChebyshevList = []
 	greedyEuclideanList = []
 	greedyChebyshevList = []
 	startTime = time.time();
	while incrementor < 100:
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

		previous, currentCost, aStarTimeComplexity, aStarSpaceComplexity = heuristics.aStarSearch(graph, startPoint, endPoint, 1)
		path = heuristics.reconstructPath(previous, startPoint, endPoint)
		if path == None:
			misses = misses + 1 
			continue
		aStarEuclideanList.append([path, aStarTimeComplexity, aStarSpaceComplexity])
		path = heuristics.reconstructPath(previous, startPoint, endPoint)
		aStarChebyshevList.append([path, aStarTimeComplexity, aStarSpaceComplexity])
		previous, greedyTimeComplexity, greedySpaceComplexity = heuristics.greedyFirstSearch(graph, startPoint, endPoint, 1)
		path = heuristics.reconstructPath(previous, startPoint, endPoint)
		greedyEuclideanList.append([path, greedyTimeComplexity, greedySpaceComplexity])
		previous, greedyTimeComplexity, greedySpaceComplexity = heuristics.greedyFirstSearch(graph, startPoint, endPoint, 2)
		path = heuristics.reconstructPath(previous, startPoint, endPoint)
		greedyChebyshevList.append([path, greedyTimeComplexity, greedySpaceComplexity])
		incrementor = incrementor + 1
	totalTime = time.time() - startTime;
	print "Total Execution Time"
	print totalTime
	print "Total Number of Invalid Paths"
	print misses
	averageTime = 0
	averageSpace = 0
	for i in aStarEuclideanList:
		averageTime = averageTime + i[1]
		averageSpace = averageSpace + i[2]
	print "Average A* Euclidean Time Complexity"
	print averageTime / len(aStarEuclideanList)
	print "Average A* Euclidean Space Complexity"
	print averageSpace / len(aStarEuclideanList)
	averageTime = 0
	averageSpace = 0
	for i in aStarChebyshevList:
		averageTime = averageTime + i[1]
		averageSpace = averageSpace + i[2]
	print "Average A* Chebyshev Time Complexity"
	print averageTime / len(aStarChebyshevList)
	print "Average A* Chebyshev Space Complexity"
	print averageSpace / len(aStarChebyshevList)
	averageTime = 0
	averageSpace = 0
	for i in greedyEuclideanList:
		averageTime = averageTime + i[1]
		averageSpace = averageSpace + i[2]
	print "Average Greedy Euclidean Time Complexity"
	print averageTime / len(greedyEuclideanList)
	print "Average Greedy Euclidean Space Complexity"
	print averageSpace / len(greedyEuclideanList)
	averageTime = 0
	averageSpace = 0
	for i in greedyChebyshevList:
		averageTime = averageTime + i[1]
		averageSpace = averageSpace + i[2]
	print "Average Greedy Chebyshev Time Complexity"
	print averageTime / len(greedyChebyshevList)
	print "Average Greedy Chebyshev Space Complexity"
	print averageSpace / len(greedyChebyshevList)
# Get 10 test results of each heuristic
	print "A* Euclidean Heuristic"
	for i in aStarEuclideanList[:10]:
		print "Path: ", i[0]
		print "Time Complexity: ", i[1]
		print "Space Complexity: ", i[2]
	print "A* Chebyshev Heuristic"
	for i in aStarChebyshevList[:10]:
		print "Path: ", i[0]
		print "Time Complexity: ", i[1]
		print "Space Complexity: ", i[2]
	print "Greedy Euclidean Heuristic"
	for i in greedyEuclideanList[:10]:
		print "Path: ", i[0]
		print "Time Complexity: ", i[1]
		print "Space Complexity: ", i[2]
	print "Greedy Chebyshev Heuristic"
	for i in greedyChebyshevList[:10]:
		print "Path: ", i[0]
		print "Time Complexity: ", i[1]
		print "Space Complexity: ", i[2]

# BFS, DFS, IDDFS benchmarks
 	breadthFirstSearchList = []
 	depthFirstSearchList = []
 	iterativeDeepeningList = []
 	misses = 0
 	incrementor = 0
 	startTime = time.time();
 	while incrementor < 100:
		startPoint = 0
		endPoint = 0
		while startPoint == endPoint:
			startPoint = chr(random.randint(0, 25) + ord('A')) 
			endPoint = chr(random.randint(0, 25) + ord('A'))
					
		mapValue = graphgeneration.randomMapGeneration()
		euclideanMap = graphgeneration.euclideanMapModify(mapValue)
		weightedGraph = graphgeneration.pruneEuclideanMap(euclideanMap)
		unWeightedGraph = graphgeneration.createUnweightedSetGrapth(weightedGraph)
		breadthFirstSearch, breadthFirstTimeComplexity, breadthFirstSearchSpaceComplexity = traverse.bfs(unWeightedGraph, startPoint, endPoint)
		if breadthFirstSearch == None:
			misses = misses + 1 
			continue
		breadthFirstSearchList.append([breadthFirstSearch, breadthFirstTimeComplexity, breadthFirstSearchSpaceComplexity])
		depthFirstSearch, depthFirstSearchTimeComplexity, depthFirstSearchSpaceComplexity = traverse.dfs(unWeightedGraph, startPoint, endPoint)
		depthFirstSearchList.append([depthFirstSearch, depthFirstSearchTimeComplexity, depthFirstSearchSpaceComplexity])
		iterativeDeeping, iterativeDeepingTimeComplexity, iterativeDeepingSpaceComplexity = traverse.id_dfs(unWeightedGraph, startPoint, endPoint)
		iterativeDeepeningList.append([iterativeDeeping, iterativeDeepingTimeComplexity, iterativeDeepingSpaceComplexity])
		incrementor = incrementor + 1
	totalTime = time.time() - startTime;
	print "Total Execution Time"
	print totalTime
	print "Total Number of Invalid Paths"
	print misses
	averageTimeBFS = 0
	averageSpaceBFS = 0
	for breadth in breadthFirstSearchList:
		averageTimeBFS = averageTimeBFS + breadth[1]
		averageSpaceBFS = averageSpaceBFS + breadth[2]
	print "Average BFS Time Complexity"
	print averageTimeBFS / len(breadthFirstSearchList)
	print "Average BFS Space Complexity"
	print averageSpaceBFS / len(breadthFirstSearchList)
	averageTimeDFS = 0
	averageSpaceDFS = 0
	for depth in depthFirstSearchList:
		averageTimeDFS = averageTimeDFS + depth[1]
		averageSpaceDFS = averageSpaceDFS + depth[2]
	print "Average DFS Time Complexity"
	print averageTimeDFS / len(depthFirstSearchList)
	print "Average DFS Space Complexity"
	print averageSpaceDFS / len(depthFirstSearchList)
	averageTimeIDDFS = 0
	averageSpaceIDDFS = 0
	for iddfs in iterativeDeepeningList:
		averageTimeIDDFS = averageTimeIDDFS + iddfs[1]
		averageSpaceIDDFS = averageSpaceIDDFS + iddfs[2]
	print "Average IDDFS Time Complexity"
	print averageTimeIDDFS / len(iterativeDeepeningList)
	print "Average IDDFS Space Complexity"
	print averageSpaceIDDFS / len(iterativeDeepeningList)
	# Get 10 results of each benchmark
	print "Breadth First Search"
	for breadth in breadthFirstSearchList[:10]:
		print "Path: ", breadth[0]
		print "Time Complexity: ", breadth[1]
		print "Space Complexity: ", breadth[2]
	print "Depth First Search"
	for depth in depthFirstSearchList[:10]:
		print "Path: ", depth[0]
		print "Time Complexity: ", depth[1]
		print "Space Complexity: ", depth[2]
	print "Iterative Deepening First Search"
	for iddfs in iterativeDeepeningList[:10]:
		print "Path: ", iddfs[0]
		print "Time Complexity: ", iddfs[1]
		print "Space Complexity: ", iddfs[2]



if __name__ == '__main__':
	main()
