import numpy

class Graph:
	"""docstring for Graph"""
	def __init__(self):
		self.edges = {}
		self.weights = {}

	def neighbors(self, id):
		return self.edges[id]

	def getWeight(self, id):
		return self.weights[id]


	def distanceToDistination(self, start, end):
		a = numpy.array(start)
		b = numpy.array(end)
		distance = numpy.linalg.norm(a - b)
		return distance
		