import random
import numpy
import heapq
import string

## 
# Generates random position for the 26 cities
##
def randomMapGeneration():
	# randomly generate coordinates for 26 cities on a 100x100 matrix
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
	# generates euclidean distance from city to city, set distance of 0.0 to 100000.0 so that later it
	# does not interfere with get the five smallest euclidean distance as it represents the distance from a city to itself
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
# @param cityList
# Generates dictionay with each cities coordinates
##
def euclideanMapValues(cityList):
	d = dict.fromkeys(string.ascii_uppercase, 0)
	for i, a in enumerate(cityList):
		d[chr(i + ord('A'))] = a
	return d

##
# @param euclideanList
# remove 2 random lowest euclidean distances 
##
def pruneEuclideanMap(euclideanList):
	euclideanFinalPruneList = []
	for i in range(len(euclideanList)):
		# creates list to store the 5 smallest euclidean distances for each city
		euclideanPruneList = []
		# finds and stores 5 smallest cities into prune list
		for j in heapq.nsmallest(5, enumerate(euclideanList[i]), key=lambda x:x[1]):
			euclideanPruneList.append(j)
		# grab three random euclidean distance from prune list
		cityPrune = random.sample(range(0, len(euclideanPruneList)), 3)
		cityEuclideanList = []
		# set the three distances as the cities edges
		for k in cityPrune:
			cityEuclideanList.append(euclideanPruneList[k])
		euclideanFinalPruneList.append(cityEuclideanList)
	# initialize euclidean matrix list
	euclideanFinalMatrix = [[0] * len(euclideanFinalPruneList) for i in range(len(euclideanFinalPruneList))]
	# reintroduce the three edges that was produced previously into the euclidean matrix
	for i in range(len(euclideanFinalPruneList)):
		for j in range(len(euclideanFinalPruneList[i])):
			euclideanFinalMatrix[i][euclideanFinalPruneList[i][j][0]] = euclideanFinalPruneList[i][j][1]
	# if there exist an directed edge from a->b create another edge from b->a to create an undirected graph
	for i in range(len(euclideanFinalMatrix)):
		for j in range(len(euclideanFinalMatrix[i])):
			if((euclideanFinalMatrix[i][j] != euclideanFinalMatrix[j][i]) and euclideanFinalMatrix[i][j] != 0):
				euclideanFinalMatrix[j][i] = euclideanFinalMatrix[i][j];
	# create a final tuple list with only valid edge tuples for each city
	euclideanFinalTupleList = []
	for i in range(len(euclideanFinalMatrix)):
		euclideanTuples = []
		for j, tupleValue in enumerate(euclideanFinalMatrix[i]):
			if(tupleValue != 0):
				euclideanTuples.append((j, tupleValue))
		euclideanFinalTupleList.append(euclideanTuples)
	return euclideanFinalTupleList


##
# @param graph
# Create a dictionary for a unweighted graph with set tuples for DFS, BFS, and ID_DFS
##
def createUnweightedSetGrapth(graph):
	# create a dictonary for A-Z
	d = dict.fromkeys(string.ascii_uppercase, 0)
	# place set tuples in thier coordinating dictionary values
	for i, a in enumerate(graph):
		listSet = []
		for j, b in enumerate(graph[i]):
			listSet.append(chr(b[0] + ord('A')))
		d[chr(i + ord('A'))] = set(listSet)
	return d

##
# @param graph
# Create a dictionary for the graph with each edge that corresponds to each city, used for A* and Greedy Best First Search
##
def createUnweightedGrapth(graph):
	# create a dictonary for A-Z
	d = dict.fromkeys(string.ascii_uppercase, 0)
	# place tuples in thier coordinating dictionary values
	for i, a in enumerate(graph):
		listGraph = []
		for j, b in enumerate(graph[i]):
			listGraph.append(chr(b[0] + ord('A')))
		d[chr(i + ord('A'))] = listGraph
	return d