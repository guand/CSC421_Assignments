from priorityqueue import PriorityQueue
from graph import Graph
import numpy

##
# Euclidean Distance Heuristic
##
def heuristicEuclidean(current, goal):
	a = numpy.array(current)
	b = numpy.array(goal)
	distance = numpy.linalg.norm(a - b)
	return distance

##
# Chebyshev Distance Heuristic
##
def heuristicChebyshev(current, goal):
	currentX, currentY = current
	goalX, goalY = goal
	a = abs(currentX - goalX)
	b = abs(currentY - goalY)
	distance = (a + b) + (-1) * min(a, b)
	return distance

##
# Greedy Best First Search
# Graph, Start, Goal, Heuristic
##
def greedyFirstSearch(graph, start, goal, heuristic):
	# initialize priority queue
	frontier = PriorityQueue()
	frontier.put(start, 0)
	previous = {}
	previous[start] = None
	# if frontier isn't empty
	while not frontier.empty():
		current = frontier.get()
		# check if current is the goal
		if current == goal:
			break
		for next in graph.neighbors(current):
			if next not in previous:
				# Greedy Best First Search will only use the heuristic to determine the path to choose
				if heuristic == 1:
			 		heuristicValue = heuristicEuclidean(graph.getWeight(current), graph.getWeight(goal))
			 	else:
			 		heuristicValue = heuristicChebyshev(graph.getWeight(current), graph.getWeight(goal))
				priority = heuristicValue
				frontier.put(next, priority)
				previous[next] = current
	return previous



##
# A* Search
# Graph, Start, Goal, and Heuristic
##
def aStarSearch(graph, start, goal, heuristic):
	# initialize Priority Queue
	frontier = PriorityQueue()
	frontier.put(start, 0)
	previous = {}
	currentCost = {}
	previous[start] = None
	currentCost[start] = 0
	# while frontier is not empty
	while not frontier.empty():
		current = frontier.get()
		if current == goal:
			break
		for next in graph.neighbors(current):
			# determine A* cost
			new_cost = currentCost[current] + graph.distanceToDistination(graph.getWeight(current), graph.getWeight(next))
			# check if the cost has gone down since last time we visited to determine if location has already been visited
			if next not in currentCost or new_cost < currentCost[next]:
			 	currentCost[next] = new_cost
				# determine which heuristic to use
			 	if heuristic == 1:
			 		heuristicValue = heuristicEuclidean(graph.getWeight(current), graph.getWeight(goal))
			 	else:
			 		heuristicValue = heuristicChebyshev(graph.getWeight(current), graph.getWeight(goal))
			 	# add heuristic cose to A* cost
			 	priority = new_cost + heuristicValue
			 	# add path with it's priority
			 	frontier.put(next, priority)
			 	previous[next] = current
	return previous, currentCost

##
# Reconstruct Path
# Previous, Start, Goal
# Reconstruct paths for A* and Greedy Best First Searches
##
def reconstructPath(previous, start, goal):
	# Reconstruct path backwards
	current = goal
	path = [current]
	# Determine the path if path does not exist return None
	while current != start:
		if current in previous:
			current = previous[current]
		else:
			return None
		path.append(current)
	path.reverse()
	return path
