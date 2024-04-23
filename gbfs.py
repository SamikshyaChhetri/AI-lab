import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, cost))

    def gbfs(self, start, goal):
        visited = set()
        priority_queue = [(0, start)]

        while priority_queue:
            _, node = heapq.heappop(priority_queue)

            if node == goal:
                print("Goal reached!")
                return

            visited.add(node)
            print("Visiting node:", node)

            if node in self.graph:
                for neighbor, cost in self.graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (cost, neighbor))

# Example usage:
g = Graph()
g.add_edge('A', 'B', 3)
g.add_edge('A', 'C', 7)
g.add_edge('B', 'D', 2)
g.add_edge('B', 'E', 8)
g.add_edge('C', 'F', 4)
g.add_edge('C', 'G', 5)

print("Starting GBFS from node A to node F:")
g.gbfs('A', 'F')
