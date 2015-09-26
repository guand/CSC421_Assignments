import random
import numpy
import heapq

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
			euclideanDistanceCities.append(distance)
		euclideanMap.append(euclideanDistanceCities)
	return euclideanMap

##
# @param euclideanList
# remove 2 random lowest euclidean distances 
##
def pruneEuclideanMap(euclideanList):
	for i, first in enumerate(euclideanList):
		euclideanPruneList = []
		for j in heapq.nsmallest(6, enumerate(euclideanList[i]), key=lambda x:x[1]):
			if (100000 >= j[1] > 0):
				euclideanPruneList.append(j[0])
		cityPrune = random.sample(range(0, len(euclideanPruneList)), 2)
		for k in cityPrune:
			euclideanList[i][euclideanPruneList[k]] = 100000.0
			euclideanList[euclideanPruneList[k]][i] = 100000.0
	for i, first in enumerate(euclideanList):
		for j, second in enumerate(euclideanList[i]):
			if(euclideanList[i][j] == 100000.0):
				euclideanList[i][j] = 0.0
	return euclideanList


mapValue = randomMapGeneration()
euclideanMap = euclideanMapModify(mapValue)
print(pruneEuclideanMap(euclideanMap))