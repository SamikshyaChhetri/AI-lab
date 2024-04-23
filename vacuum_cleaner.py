class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment
        self.location = (0, 0)  # Initial location of the agent
        self.direction = 'right'  # Initial direction of the agent

    def move(self):
        # Move the agent one step in its current direction
        x, y = self.location
        if self.direction == 'right':
            x += 1
        elif self.direction == 'left':
            x -= 1
        elif self.direction == 'up':
            y -= 1
        elif self.direction == 'down':
            y += 1

        # Check if the new location is within the environment bounds
        if 0 <= x < len(self.environment[0]) and 0 <= y < len(self.environment):
            self.location = (x, y)

    def clean(self):
        # Clean the current square of the environment
        x, y = self.location
        self.environment[y][x] = 'clean'

    def sense(self):
        # Sense the current square of the environment
        x, y = self.location
        return self.environment[y][x]

    def turn_left(self):
        # Turn the agent left
        directions = ['up', 'left', 'down', 'right']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def turn_right(self):
        # Turn the agent right
        directions = ['up', 'left', 'down', 'right']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index - 1) % 4]

# Example usage:
environment = [['dirty', 'clean', 'dirty'],
               ['clean', 'dirty', 'clean'],
               ['dirty', 'clean', 'dirty']]

agent = VacuumCleanerAgent(environment)

while True:
    state = agent.sense()
    print(f"Agent is at {agent.location} and sensing {state}")

    if state == 'dirty':
        agent.clean()
        print("Cleaning the square.")

    agent.turn_left()  # Turn left
    agent.move()       # Move forward

    if agent.location == (0, 0):
        break  # Break the loop when the agent returns to the initial position

print("Cleaning complete!")
