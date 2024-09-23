from simpleai.machine_learning.reinforcement_learning import TDQLearner, RLProblem, \
                                                             make_exponential_temperature, \
                                                             PerformanceCounter
import random
from simpleai.environments import RLEnvironment

class TicTacToeGame(RLEnvironment):
    def __init__(self, agents):
        initial_state = tuple(tuple(' ' for _ in range(3)) for _ in range(3))  # Empty 3x3 board as tuple of tuples
        super(TicTacToeGame, self).__init__(agents, initial_state)

    def do_action(self, state, action, agent):
        """Apply the agent's action to the state and return the new state."""
        if not isinstance(action, tuple) or len(action) != 2:
            raise ValueError("Action should be a tuple of (row, col)")

        new_state = [list(row) for row in state]  # Convert tuples to lists for modification
        row, col = action
        new_state[row][col] = agent.play_with
        return tuple(tuple(row) for row in new_state)  # Convert back to tuple of tuples

    def is_completed(self, state):
        """Check if the game is completed with a win or a draw."""
        for row in state:
            if row[0] == row[1] == row[2] != ' ':
                return True
        for col in range(3):
            if state[0][col] == state[1][col] == state[2][col] != ' ':
                return True
        if state[0][0] == state[1][1] == state[2][2] != ' ' or \
           state[0][2] == state[1][1] == state[2][0] != ' ':
            return True
        if all(cell != ' ' for row in state for cell in row):
            return True  # Draw
        return False

    def reward(self, state, agent):
        """Reward the agent for winning, losing, or drawing the game."""
        if self.is_completed(state):
            for row in state:
                if row[0] == row[1] == row[2] == agent.play_with:
                    return 1
            return -1
        return 0  # No reward for non-terminal states

    def percept(self, agent, state):
        """Give the agent the current state of the game."""
        return state

    def print_state(self):
        """Print the board in a grid format."""
        print("  0 1 2")
        for i, row in enumerate(self.state):
            print(f"{i} {' '.join(row)}")
    
    def print_result(self):
        """Print the result of the game."""
        if self.is_completed(self.state):
            # Determine if the game was a win or a draw
            for row in self.state:
                if row[0] == row[1] == row[2] != ' ':
                    winner = row[0]
                    if winner == 'X':
                        print("Agent wins!")
                    elif winner == 'O':
                        print("Human wins!")
                    return
            for col in range(3):
                if self.state[0][col] == self.state[1][col] == self.state[2][col] != ' ':
                    winner = self.state[0][col]
                    if winner == 'X':
                        print("Agent wins!")
                    elif winner == 'O':
                        print("Human wins!")
                    return
            if self.state[0][0] == self.state[1][1] == self.state[2][2] != ' ' or \
               self.state[0][2] == self.state[1][1] == self.state[2][0] != ' ':
                winner = self.state[1][1]
                if winner == 'X':
                    print("Agent wins!")
                elif winner == 'O':
                    print("Human wins!")
            else:
                print("It's a draw!")
        else:
            print("Game is not yet completed.")

class TicTacToeProblem(RLProblem):
    def __init__(self):
        self.possible_actions = [(row, col) for row in range(3) for col in range(3)]

    def actions(self, state):
        """Return available actions for a given state (empty spots on the board)."""
        return [(row, col) for row, col in self.possible_actions if state[row][col] == ' ']
    
    def update_state(self, percept, agent):
        """Simply return the current percept (game state) as the new state."""
        return percept
