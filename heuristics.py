from priorityqueue import PriorityQueue
from graph import Graph
import numpy

def heuristicEuclidean(current, goal):
	a = numpy.array(current)
	b = numpy.array(goal)
	distance = numpy.linalg.norm(a - b)
	return distance

def heuristicChebyshev(current, goal):
	currentX, currentY = current
	goalX, goalY = goal
	a = abs(currentX - goalX)
	b = abs(currentY - goalY)
	distance = (a + b) + (-1) * min(a, b)
	return distance


def greedyFirstSearch(graph, start, goal, heuristic):
	frontier = PriorityQueue()
	frontier.put(start, 0)
	previous = {}
	previous[start] = None

	while not frontier.empty():
		current = frontier.get()
		if current == goal:
			break
		for next in graph.neighbors(current):
			if next not in previous:
				if heuristic == 1:
			 		heuristicValue = heuristicEuclidean(graph.getWeight(current), graph.getWeight(goal))
			 	else:
			 		heuristicValue = heuristicChebyshev(graph.getWeight(current), graph.getWeight(goal))
				priority = heuristicValue
				frontier.put(next, priority)
				previous[next] = current
	return previous




def aStarSearch(graph, start, goal, heuristic):
	frontier = PriorityQueue()
	frontier.put(start, 0)
	previous = {}
	currentCost = {}
	previous[start] = None
	currentCost[start] = 0

	while not frontier.empty():
		current = frontier.get()
		if current == goal:
			break
		for next in graph.neighbors(current):
			new_cost = currentCost[current] + graph.distanceToDistination(graph.getWeight(current), graph.getWeight(next))
			if next not in currentCost or new_cost < currentCost[next]:
			 	currentCost[next] = new_cost
			 	if heuristic == 1:
			 		heuristicValue = heuristicEuclidean(graph.getWeight(current), graph.getWeight(goal))
			 	else:
			 		heuristicValue = heuristicChebyshev(graph.getWeight(current), graph.getWeight(goal))
			 	priority = new_cost + heuristicValue
			 	frontier.put(next, priority)
			 	previous[next] = current
	
	return previous, currentCost

def reconstructPath(previous, start, goal):
	current = goal
	path = [current]
	while current != start:
		if current in previous:
			current = previous[current]
		else:
			return None
		path.append(current)
	path.reverse()
	return path

# def main():
# 	test_graph = Graph()
# 	test_graph.edges = {'A': ['B', 'C'],
#          'B': ['A', 'D', 'E'],
#          'C': ['A', 'F'],
#          'D': ['B'],
#          'E': ['B', 'F'],
#          'F': ['C', 'E']}

# 	test_graph.weights = {'A': (1,2), 'B': (2,3), 'C': (3,4), 'D': (4,4), 'E': (0,0), 'F': (3,1)}

# 	previous, currentCost = aStarSearch(test_graph, 'A', 'F', 2)
 
# 	print reconstructPath(previous, 'A', 'F')

# 	previous = greedyFirstSearch(test_graph, 'A', 'F', 2)
# 	print reconstructPath(previous, 'A', 'F')
# 	heuristicChebyshev((1,2), (3,4))

# if __name__ == '__main__':
# 	main()