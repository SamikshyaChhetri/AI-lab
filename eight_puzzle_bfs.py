from collections import deque

class Puzzle:
    def __init__(self, state):
        self.state = state

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def move(self, direction):
        x, y = self.get_blank_position()
        new_state = [row[:] for row in self.state]

        if direction == 'up' and x > 0:
            new_state[x][y], new_state[x-1][y] = new_state[x-1][y], new_state[x][y]
        elif direction == 'down' and x < 2:
            new_state[x][y], new_state[x+1][y] = new_state[x+1][y], new_state[x][y]
        elif direction == 'left' and y > 0:
            new_state[x][y], new_state[x][y-1] = new_state[x][y-1], new_state[x][y]
        elif direction == 'right' and y < 2:
            new_state[x][y], new_state[x][y+1] = new_state[x][y+1], new_state[x][y]

        return Puzzle(new_state)

    def get_possible_moves(self):
        directions = ['up', 'down', 'left', 'right']
        return [self.move(dir) for dir in directions if self.is_valid_move(dir)]

    def is_valid_move(self, direction):
        x, y = self.get_blank_position()
        return (direction == 'up' and x > 0) or \
               (direction == 'down' and x < 2) or \
               (direction == 'left' and y > 0) or \
               (direction == 'right' and y < 2)

def breadth_first_search(initial_state):
    queue = deque([initial_state])
    visited = set()

    while queue:
        current_node = queue.popleft()
        visited.add(current_node)

        if current_node.state == goal_state.state:
            return current_node

        for child in current_node.get_possible_moves():
            if child not in visited:
                queue.append(child)

    return None

# Example initial and goal states
initial_state = Puzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
goal_state = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

# Solve using Breadth-First Search
result_bfs = breadth_first_search(initial_state)
print("BFS Solution:")
if result_bfs is not None:
    print(result_bfs.state)
else:
    print("No solution found.")
