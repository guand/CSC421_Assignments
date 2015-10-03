
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
	space = 0
	while stack:
		# get space complexity
		space = max(space, len(stack))
		# pop city from stack
		(vertex, path) = stack.pop()
		for next in graph[vertex] - set(path):
			# return path and time complexity onced reached
			if next == goal:
				count = count + 1
				return path + [next], count, space
			else:
				stack.append((next, path + [next]))
				count = count + 1;
	return None, count, space

##
# Breadth First Search
# With Graph, Start, and Goal
# return Path, Time Complexity, and Space Complexity
##
def bfs(graph, start, goal):
	# initialize queue and time complexity
	queue = [(start, [start])]
	count = 1
	space = 0
	while queue:
		# get space complexity
		space = max(space, len(queue))
		# dequeued first city in the queue
		(vertex, path) = queue.pop(0)
		for next in graph[vertex] - set(path):
			if next == goal:
				count = count + 1
				return path + [next], count, space
			else:
				queue.append((next, path + [next]))
				count = count + 1;
	return None, count, space
				

##
# Iterative Deepening Depth First Search
# With Graph, Start, and Goal
# return Path, Time Complexity, and Space Complexity
##
def id_dfs(graph, start, goal):
	##
	# Depth First Search for Iterative Deepening
	# With Grapth, Start, Goal, Current Time Complexity, and current path
	# local function
	##
	def dfs_depth(graph, start, goal, depth, curr, space, path=None):
		totalSpace = 0
		if path != None:
			# check if goal is found
			if goal == path[-1]:
				return path, curr, space
		if depth >= 0:
			if path == None:
				path = [start]
			if goal == path[-1]:
				return path, curr, space
			# set current space complexity
			totalSpace = space
			for next in graph[start] - set(path):
				# recursively use Depth First Search till a path is found
				route, curr, space = dfs_depth(graph, next, goal, depth-1, curr + 1, space + 1, path + [next])
				if route:
					return route, curr, space
			# reset current space complexity
			space = totalSpace
		return None, curr, space

	# intialize depth, solution, and time complexity
	depth = 0
	solution = None
	curr = 1
	totalCurr = 0
	totalSpace = 0
	space = 0
	temp = 0
	# increase depth till solution is found or till depth is the size of the graph and no solution is found
	while not solution:
		if depth == len(graph):
			break
		# grab the path and time complexity from the modified depth first search
		temp = space
		solution, curr, space = dfs_depth(graph, start, goal, depth, curr, space + 1)
		depth = depth + 1
		totalCurr = curr + totalCurr
		totalSpace = max(totalSpace, space)
		space = temp
	return solution, totalCurr, totalSpace

	


