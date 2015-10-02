import numpy

class Graph:
	"""docstring for Graph"""
	def __init__(self):
		self.edges = {}
		self.weights = {}

	# return neighbors for city
	def neighbors(self, id):
		return self.edges[id]

	# return weight for city
	def getWeight(self, id):
		return self.weights[id]

	# return euclidean distance from a given start location and a given end location
	def distanceToDistination(self, start, end):
		a = numpy.array(start)
		b = numpy.array(end)
		distance = numpy.linalg.norm(a - b)
		return distance
		