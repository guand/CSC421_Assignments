import random
import numpy
import heapq
import string
import time
## 
# Generates random position for the 25 cities
##
def randomMapGeneration():
	random.seed()
	while True:
		randomCityMap = [(random.randint(0, 100), random.randint(0, 100)) for k in range(26)]
		if len(randomCityMap)!=len(set(randomCityMap)):
			break
	return randomCityMap

##
# @param cityList
# Generates the euclidean distance for each city
##
def euclideanMapModify(cityList):
	euclideanMap = []
	for i, first in enumerate(cityList):
		euclideanDistanceCities = []
		for j, second in enumerate(cityList):
			a = numpy.array(first)
			b = numpy.array(second)
			distance = numpy.linalg.norm(a - b)
			if(distance == 0.0):
				distance = 100000.0
			euclideanDistanceCities.append(distance)
		euclideanMap.append(euclideanDistanceCities)
	return euclideanMap

##
# @param euclideanList
# remove 2 random lowest euclidean distances 
##
def pruneEuclideanMap(euclideanList):
	euclideanFinalPruneList = []
	for i, first in enumerate(euclideanList):
		euclideanPruneList = []
		for j in heapq.nsmallest(5, enumerate(euclideanList[i]), key=lambda x:x[1]):
			euclideanPruneList.append(j)
		cityPrune = random.sample(range(0, len(euclideanPruneList)), 3)
		cityEuclideanList = []
		for k in cityPrune:
			cityEuclideanList.append(euclideanPruneList[k])
		euclideanFinalPruneList.append(cityEuclideanList)
# make adjacency matrix so that we can remove undirected edges
	euclideanFinalMatrix = [[0] * len(euclideanFinalPruneList) for i in range(len(euclideanFinalPruneList))]
	for i in range(len(euclideanFinalPruneList)):
		for j in range(len(euclideanFinalPruneList[i])):
			euclideanFinalMatrix[i][euclideanFinalPruneList[i][j][0]] = euclideanFinalPruneList[i][j][1]
	for i in range(len(euclideanFinalMatrix)):
		for j in range(len(euclideanFinalMatrix[i])):
			if((euclideanFinalMatrix[i][j] != euclideanFinalMatrix[j][i]) and euclideanFinalMatrix[i][j] != 0):
				euclideanFinalMatrix[j][i] = euclideanFinalMatrix[i][j];
	euclideanFinalTupleList = []
	for i, value in enumerate(euclideanFinalMatrix):
		euclideanTuples = []
		for j, tupleValue in enumerate(euclideanFinalMatrix[i]):
			if(tupleValue != 0):
				euclideanTuples.append((j, tupleValue))
		euclideanFinalTupleList.append(euclideanTuples)
	return euclideanFinalTupleList

def createUnweightedGrapth(graph):
	d = dict.fromkeys(string.ascii_uppercase, 0)
	for i, a in enumerate(graph):
		listSet = []
		for j, b in enumerate(graph[i]):
			listSet.append(chr(b[0] + ord('A')))
		d[chr(i + ord('A'))] = set(listSet)
	return d

def dfs(graph, start, goal):
	stack = [(start, [start])]
	count = 1
	while stack:
		(vertex, path) = stack.pop()
		for next in graph[vertex] - set(path):
			if next == goal:
				count = count + 1
				return path + [next], count
			else:
				stack.append((next, path + [next]))
				count = count + 1;
	return None, count

def bfs(graph, start, goal):
	queue = [(start, [start])]
	count = 1;
	while queue:
		(vertex, path) = queue.pop(0)
		for next in graph[vertex] - set(path):

			if next == goal:
				count = count + 1
				return path + [next], count
			else:
				queue.append((next, path + [next]))
				count = count + 1;
	return None, count
				


def id_dfs(graph, start, goal):
	depth = 0
	solution = None
	curr = 1
	totalCurr = 0;
	while not solution:
		if depth == len(graph):
			break
		solution, curr = dfs_depth(graph, start, goal, curr, depth)
		depth = depth + 1
		totalCurr = curr + totalCurr
	return solution, totalCurr


def dfs_depth(graph, start, goal, depth, curr, path=None):
	if path != None:
		if goal == path[-1]:
			curr = curr + 1
			return path, curr
	if depth >= 0:
		if path == None:
			path = [start]
		if goal == path[-1]:
			return path, curr
		for next in graph[start] - set(path):
			route, curr = dfs_depth(graph, next, goal, depth-1, curr + 1, path + [next])
			if route:
				return route, curr
	return None, curr


def main():
	# mapValue = randomMapGeneration()
	# euclideanMap = euclideanMapModify(mapValue)
	# weightedGraph = pruneEuclideanMap(euclideanMap)
	# unWeightedGraph = createUnweightedGrapth(weightedGraph)

	# graph = {'A': set(['B', 'C']),
 #         'B': set(['A', 'D', 'E']),
 #         'C': set(['A', 'F']),
 #         'D': set(['B']),
 #         'E': set(['B', 'F']),
 #         'F': set(['C', 'E'])}
 	
 	for i in range(100):
		startPoint = 0
		endPoint = 0
		while startPoint == endPoint:
			startPoint = chr(random.randint(0, 25) + ord('A')) 
			endPoint = chr(random.randint(0, 25) + ord('A'))
					
		mapValue = randomMapGeneration()
		euclideanMap = euclideanMapModify(mapValue)
		weightedGraph = pruneEuclideanMap(euclideanMap)
		unWeightedGraph = createUnweightedGrapth(weightedGraph)
		startTime = time.time();
		breadthFirstSearch, breadthFirstTimeComplexity = bfs(unWeightedGraph, startPoint, endPoint)
		totalTime = time.time() - startTime;
		print "Breadth First Search"
		print breadthFirstSearch
		print breadthFirstTimeComplexity
		print totalTime
		startTime = time.time();
		depthFirstSearch, depthFirstSearchTimeComplexity = dfs(unWeightedGraph, startPoint, endPoint)
		totalTime = time.time() - startTime;
		print "Depth First Search"
		print depthFirstSearch
		print depthFirstSearchTimeComplexity
		print totalTime
		startTime = time.time();
		iterativeDeeping, iterativeDeepingTimeComplexity = id_dfs(unWeightedGraph, startPoint, endPoint)
		totalTime = time.time() - startTime;
		print "Iterative Deeping"
		print iterativeDeeping
		print iterativeDeepingTimeComplexity
		print totalTime



if __name__ == '__main__':
	main()
