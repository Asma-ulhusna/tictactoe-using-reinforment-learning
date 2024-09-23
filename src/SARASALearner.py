from simpleai.machine_learning.reinforcement_learning import SARSALearner, RLProblem, \
                                                             make_exponential_temperature, \
                                                             PerformanceCounter
import random
from simpleai.environments import RLEnvironment


class TicTacToePlayer(SARSALearner):
    def __init__(self, play_with, *args, **kwargs):
        problem = TicTacToeProblem()
        super(TicTacToePlayer, self).__init__(problem, *args, **kwargs)
        self.play_with = play_with

class RandomPlayer:
    def __init__(self, play_with):
        self.play_with = play_with

    def program(self, state):
        """Randomly choose an available position."""
        available_actions = [(row, col) for row in range(3) for col in range(3) if state[row][col] == ' ']
        return random.choice(available_actions) if available_actions else None

    def set_reward(self, reward, completed):
        pass

class HumanPlayer:
    def __init__(self, play_with):
        self.play_with = play_with

    def program(self, state):
        """Allow a human to input their move."""
        print("Current state:")
        print_grid(state)
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if state[row][col] == ' ':
                    return (row, col)
                else:
                    print("Cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

    def set_reward(self, reward, completed):
        print(('reward:', reward))

def print_grid(state):
    """Print the board in a grid format."""
    print("   0   1   2")
    print(" +---+---+---+")
    for i, row in enumerate(state):
        row_display = f"{i}| {' | '.join(row)} |"
        print(row_display)
        print(" +---+---+---+")

if __name__ == '__main__':
    # Initialize players
    a = TicTacToePlayer('X', temperature_function=make_exponential_temperature(1, 0.01))
    b = RandomPlayer('O')
    c = HumanPlayer('O')
    
    # Initialize the Tic-Tac-Toe game environment
    game = TicTacToeGame([a, b])
    
    # Training phase (SARSA agent vs Random player)
    print('Training with a random player, please wait...')
    game.agents = [a, b]
    for i in range(3000):
        game.run()
    
    # Save the trained SARSA agent
    a.dump('sarsa_agent')
    
    # Load the trained SARSA agent
    d = TicTacToePlayer.load('sarsa_agent')
    d.play_with = 'O'
    
    # Evaluation phase (SARSA agent vs Random player)
    game.agents = [a, d]
    per = PerformanceCounter(game.agents, ['SARSA_A', 'SARSA_D'])
    for i in range(3000):
        game.run()
    per.show_statistics()
    
    # Evaluation phase (SARSA agent vs Human player)
    game.agents = [a, c]
    print('Do you like to play with SARSA Agent?')
    game.run()
    print("Final state:")
    game.print_state()
    game.print_result()  # This should be manually handled if not available in your setup
