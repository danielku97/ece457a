#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by Daniel Ku
# ECE 457A A1

def upBfs(maze, init, queue, visited, destination):
	position = [init[0],init[1]]
	if position[0] == 0:
		return False
	if maze[position[0] - 1][position[1]] == 1 or visited[position[0] - 1][position[1]] != None:
		return False
	else:
		position[0] = position[0] - 1
		visited[position[0]][position[1]] = [init[0],init[1]]
		queue.append(position)

		if position == destination:
			return True
		else:
			return False

def downBfs(maze, init, queue, visited, destination):
	position = [init[0],init[1]]
	if position[0] == 24:
		return False
	if maze[position[0] + 1][position[1]] == 1 or visited[position[0] + 1][position[1]] != None:
		return False
	else:
		position[0] = position[0] + 1
		visited[position[0]][position[1]] = [init[0],init[1]]
		queue.append(position)

		if position == destination:
			return True
		else:
			return False

def leftBfs(maze, init, queue, visited, destination):
	position = [init[0],init[1]]
	if position[1] == 0:
		return False
	if maze[position[0]][position[1] - 1] == 1 or visited[position[0]][position[1] - 1] != None:
		return False
	else:
		position[1] = position[1] - 1
		visited[position[0]][position[1]] = [init[0],init[1]]
		queue.append(position)

		if position == destination:
			return True
		else:
			return False

def rightBfs(maze, init, queue, visited, destination):
	position = [init[0],init[1]]
	if position[1] == 24:
		return False
	if maze[position[0]][position[1] + 1] == 1 or visited[position[0]][position[1] + 1] != None:
		return False
	else:
		position[1] = position[1] + 1
		visited[position[0]][position[1]] = [init[0],init[1]]
		queue.append(position)

		if position == destination:
			return True
		else:
			return False

def printFinalPath(startPosition, endPosition, visited):
	stack = [endPosition]
	print("Printing Final Path:")
	running = True
	while running:
		if endPosition == startPosition:
			running = False
			break
		stack.append(visited[endPosition[0]][endPosition[1]])
		endPosition = visited[endPosition[0]][endPosition[1]]
	stack.reverse()
	print(stack)
	print(f"Solution Cost : {len(stack)} nodes")

def bfs(startPosition, endPosition):
	# Initialized visited array to be all zeros
	print("Running BFS Algorithm")
	visited = [ [None] * 25 for _ in range(25)]
	queue = []
	queue.append(startPosition)
	possiblePath = False
	counter = 0

	while len(queue) != 0:
		temp = queue.pop(0)
		counter = counter + 1
		test1 = upBfs(maze, temp, queue, visited, endPosition)
		test2 = downBfs(maze, temp, queue, visited, endPosition)
		test3 = leftBfs(maze, temp, queue, visited, endPosition)
		test4 = rightBfs(maze, temp, queue, visited, endPosition)
		if test1 or test2 or test3 or test4:
			possiblePath = True
			break

	print(f"Possible path from {startPosition} to {endPosition} : {possiblePath}")
	if possiblePath:
		printFinalPath(startPosition,endPosition,visited)
	# Spacing
	print(f"Total Nodes Explored : {counter}")
	print("\n")

def resetDFSCounter():
	global DFScounter
	DFScounter = 0

def dfs(startPosition, endPosition):
	print("Running DFS Algorithm")
	visited = [ [None] * 25 for _ in range(25)]
	possiblePath = dfsAlgo(maze, startPosition, visited, endPosition, None)

	print(f"Possible path from {startPosition} to {endPosition} : {possiblePath}")
	if possiblePath:
		printFinalPath(startPosition,endPosition,visited)
	# Spacing
	print(f"Total Nodes Explored : {DFScounter}")
	print("\n")
	resetDFSCounter()

def dfsAlgo(maze, init, visited, endPosition, prev):
	global DFScounter
	position = [init[0], init[1]]
	if (visited[position[0]][position[1]] != None):
		return False

	if prev != None:
		visited[init[0]][init[1]] = [prev[0], prev[1]]

	DFScounter = DFScounter + 1

	if (position[0] == endPosition[0] and position[1] == endPosition[1]):
		return True


	up = position[0] - 1
	down = position[0] + 1
	right = position[1] + 1
	left = position[1] - 1

	# Lets just prioritize down, right, up, left, since most goals go that direction
	
	# Down
	if (down <= 24 and maze[down][position[1]] == 0):
		if (dfsAlgo(maze, [down, position[1]], visited, endPosition, [position[0], position[1]])):
			return True

	# Right
	if (right <= 24 and maze[position[0]][right] == 0):
		if (dfsAlgo(maze, [position[0], right], visited, endPosition, [position[0], position[1]])):
			return True

	# Up
	if (up >= 0 and maze[up][position[1]] == 0):
		if (dfsAlgo(maze, [up, position[1]], visited, endPosition, [position[0], position[1]])):
			return True

	# Left
	if (left >= 0 and maze[position[0]][left] == 0):
		if (dfsAlgo(maze, [position[0], left], visited, endPosition, [position[0], position[1]])):
			return True
	return False

def upHeuristic(maze, init, queue, heuristic, counter):
	position = [init[0],init[1]]
	if position[0] == 0:
		return
	if maze[position[0] - 1][position[1]] == 1 or heuristic[position[0] - 1][position[1]] != None:
		return
	else:
		position[0] = position[0] - 1
		heuristic[position[0]][position[1]] = counter
		queue.append(position)

def downHeuristic(maze, init, queue, heuristic, counter):
	position = [init[0],init[1]]
	if position[0] == 24:
		return
	if maze[position[0] + 1][position[1]] == 1 or heuristic[position[0] + 1][position[1]] != None:
		return
	else:
		position[0] = position[0] + 1
		heuristic[position[0]][position[1]] = counter
		queue.append(position)

def leftHeuristic(maze, init, queue, heuristic, counter):
	position = [init[0],init[1]]
	if position[1] == 0:
		return
	if maze[position[0]][position[1] - 1] == 1 or heuristic[position[0]][position[1] - 1] != None:
		return 
	else:
		position[1] = position[1] - 1
		heuristic[position[0]][position[1]] = counter
		queue.append(position)

def rightHeuristic(maze, init, queue, heuristic, counter):
	position = [init[0],init[1]]
	if position[1] == 24:
		return
	if maze[position[0]][position[1] + 1] == 1 or heuristic[position[0]][position[1] + 1] != None:
		return
	else:
		position[1] = position[1] + 1
		heuristic[position[0]][position[1]] = counter
		queue.append(position)

def aStar(startPosition, endPosition):
	print("Running A* Algorithm")
	# Let's use the current BFS implementation to create a perfect heuristic stemming from the endpoint
	visited = [ [None] * 25 for _ in range(25)]
	heuristic = perfectHeuristicGeneration(endPosition)
	# Manually verfied heuristic is perfect and what I expected
	# Since g(n) always = 1, our function is essentially h(n)
	# We can 'hill climb' to a lower h(n) every step

	stack = [startPosition]
	heuristicCounter = heuristic[startPosition[0]][startPosition[1]]

	if heuristicCounter == None:
		print("No possible path exists")
		return
	else:
		print(f"Possible path from {startPosition} to {endPosition} : True")

	yPos = startPosition[0]
	xPos = startPosition[1]

	while(heuristicCounter != 0):
		up = yPos - 1
		down = yPos + 1
		left = xPos - 1
		right = xPos + 1

		# Up
		if up >= 0 and heuristic[up][xPos] == heuristicCounter - 1:
			yPos = yPos - 1
			heuristicCounter = heuristicCounter - 1
			stack.append([yPos, xPos])

		# Right
		if right <= 24 and heuristic[yPos][right] == heuristicCounter - 1:
			xPos = xPos + 1
			heuristicCounter = heuristicCounter - 1
			stack.append([yPos, xPos])

		# Down
		if down <= 24 and heuristic[down][xPos] == heuristicCounter - 1:
			yPos = yPos + 1
			heuristicCounter = heuristicCounter - 1
			stack.append([yPos, xPos])

		# Left
		if left >= 0 and heuristic[yPos][left] == heuristicCounter - 1:
			xPos = xPos - 1
			heuristicCounter = heuristicCounter - 1
			stack.append([yPos, xPos])

	print("Printing Final Path:")
	print(stack)
	print(f"Solution Cost: {len(stack)} nodes")
	print(f"Total Nodes Explored: {len(stack)}")
	print("\n")

def perfectHeuristicGeneration(endPosition):
	heuristic = [ [None] * 25 for _ in range(25)]
	heuristic[endPosition[0]][endPosition[1]] = 0
	queue = []
	queue.append(endPosition)
	counter = -1	

	while len(queue) != 0:
		temp = queue.pop(0)
		counter = heuristic[temp[0]][temp[1]] + 1
		test1 = upHeuristic(maze, temp, queue, heuristic, counter)
		test2 = downHeuristic(maze, temp, queue, heuristic, counter)
		test3 = leftHeuristic(maze, temp, queue, heuristic, counter)
		test4 = rightHeuristic(maze, temp, queue, heuristic, counter)

	return heuristic


# MAIN

# Initialize Testing Maze (Flipped so (0,0) is top left, (24,24) is bottom right)
# 0 = free, 1 = wall
maze = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
[0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
[1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
[1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0],
[0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0],
[0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1],
[0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
]
DFScounter = 0

bfs([11,2], [19,23])
bfs([11,2], [21,2])
bfs([0,0], [24,24])
dfs([11,2], [19,23])
dfs([11,2], [21,2])
dfs([0,0], [24,24])
aStar([11,2], [19,23])
aStar([11,2], [21,2])
aStar([0,0], [24,24])