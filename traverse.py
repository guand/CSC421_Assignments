
##
# Depth First Search 
# With Graph, Start, and Goal
# return Path, Time Complexity, and Space Complexity
##
def dfs(graph, start, goal):
	# initialize stack
	stack = [(start, [start])]
	# intialize time complexity counter
	count = 1
	while stack:
		(vertex, path) = stack.pop()
		# make sure 
		for next in graph[vertex] - set(path):
			# return path and time complexity onced reached
			if next == goal:
				count = count + 1
				return path + [next], count
			else:
				stack.append((next, path + [next]))
				count = count + 1;
	return None, count

##
# Breadth First Search
# With Graph, Start, and Goal
# return Path, Time Complexity, and Space Complexity
##
def bfs(graph, start, goal):
	# initialize queue and time complexity
	queue = [(start, [start])]
	count = 1;
	while queue:
		# dequeued first city in the queue
		(vertex, path) = queue.pop(0)
		for next in graph[vertex] - set(path):
			if next == goal:
				count = count + 1
				return path + [next], count
			else:
				queue.append((next, path + [next]))
				count = count + 1;
	return None, count
				

##
# Iterative Deepening Depth First Search
# With Graph, Start, and Goal
# return Path, Time Complexity, and Space Complexity
##
def id_dfs(graph, start, goal):
	# intialize depth, solution, and time complexity
	depth = 0
	solution = None
	curr = 1
	totalCurr = 0;
	# increase depth till solution is found or till depth is the size of the graph and no solution is found
	while not solution:
		if depth == len(graph):
			break
		# grab the path and time complexity from the modified depth first search
		solution, curr = dfs_depth(graph, start, goal, curr, depth)
		depth = depth + 1
		totalCurr = curr + totalCurr
	return solution, totalCurr


##
# Depth First Search for Iterative Deepening
# With Grapth, Start, Goal, Current Time Complexity, and current path 
##
def dfs_depth(graph, start, goal, depth, curr, path=None):
	if path != None:
		# check if goal is found
		if goal == path[-1]:
			curr = curr + 1
			return path, curr
	if depth >= 0:
		if path == None:
			path = [start]
		if goal == path[-1]:
			return path, curr
		for next in graph[start] - set(path):
			# recursively use Depth First Search till a path is found
			route, curr = dfs_depth(graph, next, goal, depth-1, curr + 1, path + [next])
			if route:
				return route, curr
	return None, curr