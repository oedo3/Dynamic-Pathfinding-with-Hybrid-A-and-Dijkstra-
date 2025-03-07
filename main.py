import heapq
import random

class Graph:
	def __init__(self):
		self.edges = {}

	def add_edge(self, from_node, to_node, weight):
		if from_node not in self.edges:
			self.edges[from_node] = []
		self.edges[from_node].append((to_node, weight))

	def get_neighbors(self, node):
		return self.edges.get(node, [])

	def update_edge(self, from_node, to_node, new_weight):
		if from_node in self.edges:
			for i, (neighbor, weight) in enumerate(self.edges[from_node]):
				if neighbor == to_node:
					self.edges[from_node][i] = (to_node, new_weight)

def heuristic(node, goal):
	# Example heuristic: Manhattan distance
	return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def a_star(graph, start, goal):
	open_set = []
	heapq.heappush(open_set, (0 + heuristic(start, goal), start))
	came_from = {}
	g_score = {start: 0}

	while open_set:
		_, current = heapq.heappop(open_set)

		if current == goal:
			return reconstruct_path(came_from, current)

		for neighbor, weight in graph.get_neighbors(current):
			tentative_g_score = g_score[current] + weight
			if tentative_g_score < g_score.get(neighbor, float('inf')):
				came_from[neighbor] = current
				g_score[neighbor] = tentative_g_score
				heapq.heappush(open_set, (g_score[neighbor] + heuristic(neighbor, goal), neighbor))

	return None  # No path found

def dijkstra(graph, start, goal):
	open_set = []
	heapq.heappush(open_set, (0, start))
	came_from = {}
	g_score = {start: 0}

	while open_set:
		_, current = heapq.heappop(open_set)

		if current == goal:
			return reconstruct_path(came_from, current)

		for neighbor, weight in graph.get_neighbors(current):
			tentative_g_score = g_score[current] + weight
			if tentative_g_score < g_score.get(neighbor, float('inf')):
				came_from[neighbor] = current
				g_score[neighbor] = tentative_g_score
				heapq.heappush(open_set, (g_score[neighbor], neighbor))

	return None  # No path found

def hybrid_a_star_dijkstra(graph, start, goal, dynamic_update):
	use_a_star = True
	path = None

	while True:
		if use_a_star:
			print("Running A*...")
			path = a_star(graph, start, goal)
		else:
			print("Switching to Dijkstra...")
			path = dijkstra(graph, start, goal)

		if path:
			print(f"Path found: {path}")
			return path

		# Simulate dynamic graph changes
		dynamic_update(graph)
		use_a_star = not use_a_star  # Switch algorithm

def reconstruct_path(came_from, current):
	path = [current]
	while current in came_from:
		current = came_from[current]
		path.append(current)
	path.reverse()
	return path

# Example Usage
graph = Graph()
graph.add_edge((0, 0), (0, 1), 1)
graph.add_edge((0, 1), (0, 2), 1)
graph.add_edge((0, 2), (1, 2), 1)
graph.add_edge((1, 2), (2, 2), 1)
graph.add_edge((0, 0), (1, 0), 4)
graph.add_edge((1, 0), (1, 1), 1)
graph.add_edge((1, 1), (1, 2), 1)

# Dynamic graph update simulation
def dynamic_update(graph):
	print("Dynamic update: Changing edge weight!")
	graph.update_edge((0, 1), (0, 2), random.randint(2, 5))  # Change weight dynamically

start = (0, 0)
goal = (2, 2)

hybrid_a_star_dijkstra(graph, start, goal, dynamic_update)


###
#raph = Graph()

# Define a 5x5 grid with random weights for more complexity
#nodes = [(x, y) for x in range(5) for y in range(5)]

# Add edges for all adjacent nodes in the grid
#for x, y in nodes:
#	if x < 4:  # Add edge to the right
#		graph.add_edge((x, y), (x + 1, y), random.randint(1, 5))
#		graph.add_edge((x + 1, y), (x, y), random.randint(1, 5))  # Bidirectional
#	if y < 4:  # Add edge downward
#		graph.add_edge((x, y), (x, y + 1), random.randint(1, 5))
#		graph.add_edge((x, y + 1), (x, y), random.randint(1, 5))  # Bidirectional
#
## Dynamic graph update simulation
#def dynamic_update(graph):
#	print("Dynamic update: Changing random edge weights!")
#	Randomly update weights of 2 random edges
#	for _ in range(2):
#		from_node = (random.randint(0, 4), random.randint(0, 4))
#		to_node = (from_node[0] + random.choice([0, 1]), from_node[1] + random.choice([0, #1]))
#		if (0 <= to_node[0] < 5) and (0 <= to_node[1] < 5):
#			graph.update_edge(from_node, to_node, random.randint(2, 8))
#
#start = (0, 0)
#goal = (4, 4)
#
#hybrid_a_star_dijkstra(graph, start, goal, dynamic_update)
###
