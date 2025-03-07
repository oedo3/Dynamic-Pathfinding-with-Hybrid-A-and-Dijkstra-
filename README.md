# Dynamic-Pathfinding-with-Hybrid-A-and-Dijkstra
This Python project combines A* and Dijkstra’s algorithms for adaptive pathfinding in dynamic graphs, using Manhattan distance for A*. It dynamically switches between algorithms based on real-time graph updates, ideal for map applications, game development, and real-time systems.

Key Components:
Graph Class:
1. Models a graph with nodes and weighted edges.
Allows edge additions, neighbor retrieval, and dynamic updates to edge weights.
A Algorithm*:

2. Uses a heuristic (Manhattan distance) to find the shortest path.
Efficiently searches by combining the actual cost and heuristic estimation.
Dijkstra’s Algorithm:

3. Computes the shortest path by exploring all possible routes and updating the minimum cost path.
Hybrid A and Dijkstra*:

4. Dynamically switches between A* and Dijkstra based on graph updates. This helps in exploring different paths when changes are made to the graph (such as edge weight modifications).

5. Dynamic Graph Update:
Simulates random updates in edge weights during the pathfinding process, allowing the system to adjust in real-time.

Example Usage:
A simple 2D grid graph is created with nodes and weighted edges.
A hybrid pathfinding process starts at a node (0, 0) and aims to reach (2, 2), with random weight changes to the graph during the process.
Key Features:
Graph Construction: Define your graph with weighted edges.
Pathfinding: Switches between A* and Dijkstra based on the graph's state.
Heuristic-based Search: Uses Manhattan distance for A* to prioritize nodes closer to the goal.
Dynamic Updates: Simulate real-time changes in the graph to test the system's adaptability.

Example Graph:
graph.add_edge((0, 0), (0, 1), 1)
graph.add_edge((0, 1), (0, 2), 1)
graph.add_edge((0, 2), (1, 2), 1)

Dynamic Update Function:
def dynamic_update(graph):
    print("Dynamic update: Changing edge weight!")
    graph.update_edge((0, 1), (0, 2), random.randint(2, 5))  # Random weight change
