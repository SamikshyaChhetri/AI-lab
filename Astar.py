import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, cost))

        # Adding bidirectional edges for unidirectional graph
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append((u, cost))

    def astar(self, start, goal, heuristic):
        priority_queue = [(0, start)]
        visited = set()
        g_score = {node: float('inf') for node in self.graph}
        g_score[start] = 0
        f_score = {node: float('inf') for node in self.graph}
        f_score[start] = heuristic(start, goal)

        while priority_queue:
            _, current = heapq.heappop(priority_queue)

            if current == goal:
                print("Goal reached!")
                return

            visited.add(current)

            if current in self.graph:
                for neighbor, cost in self.graph[current]:
                    tentative_g_score = g_score[current] + cost
                    if tentative_g_score < g_score.get(neighbor, float('inf')):
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                        heapq.heappush(priority_queue, (f_score[neighbor], neighbor))

# Example usage:
def heuristic(node, goal):
    # Manhattan distance heuristic
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

g = Graph()
g.add_edge((0, 0), (1, 0), 1)
g.add_edge((0, 0), (0, 1), 1)
g.add_edge((1, 0), (1, 1), 1)
g.add_edge((1, 1), (0, 1), 1)
g.add_edge((1, 0), (0, 0), 1)  # Ensure bidirectional edges for all nodes
g.add_edge((0, 1), (0, 0), 1)
g.add_edge((1, 1), (1, 0), 1)
g.add_edge((0, 1), (1, 1), 1)

print("Starting A* from (0, 0) to (1, 1):")
g.astar((0, 0), (1, 1), heuristic)
