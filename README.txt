*Tic-Tac-Toe Reinforcement Learning with SimpleAI*
-----------------------------------------------------------------------------------------------------------------------------

## Introduction
===============
This project presents the implementation, and evaluation of two well-known reinforcement learning algorithms implementing the SimpleAI library as TD-Q Learning and SARSA. SimpleAI library provides RL-Environment for development and testing of the algorithms similar to open AI Gym. The agents will acquire the game of Tic-Tac-Toe from the environment, which they will do by storing their rewards in a q-table that represents the state action pairs of the agents depending on how well they perform. The TD-Q learning agent outperformed the SARSA agent in terms of the success of the agent in the games and its learning capabilities. 



### Libraries Used
==================
The following libraries are essential for the project:
   |-> Python Standard Libraries:
       1. random: Used to generate random moves and actions during training.
          -------
   |-> Third-Party Libraries:
        1. SimpleAI:
           =========
            TDQLearner: This class implements TD-Q Learning for the agent.
            -----------
            SARSALearner: This class implements SARSA for the agent.
            ------------
            RLProblem: Defines the reinforcement learning problem, managing states, actions, and rewards.
            ----------
            make_exponential_temperature: This function generates an exponential temperature curve, for controlling exploration exploitation tradeoff.
            ------------------
            PerformanceCounter: This class is used to track and evaluate agent performance based on accumulated rewards and states and evaluation is used to present graphs.
            -------------------
            RLEnvironment: This is the environment where the Tic-Tac-Toe game is played and where the agents interact.
            -------------
            matplotlib: Used to create plots that visualize agent performance over time, based on various metrices
            -----------
            numpy: Handles numerical calculations for performance tracking.
            -----
            pickle: Saves and loads Q-values for the agents, preserving their learned strategies.
            -------


#### Installation
==================
->Install the required dependencies:
    pip install -r requirements.txt

->Install matplotlib and numpy if necessary:
    pip install matplotlib numpy


##### Tic-Tac-Toe Environment
==============================
The Tic-Tac-Toe environment is built using the RLEnvironment class of the SimpleAI library. This environment has some classes that are  game states, possible actions, rewards and i have included additional classes to make it interactive such as print_state , print_result and percept. Agents can interact with this environment, learning optimal strategies for winning by accumulating rewards over a number of training episodes.

###### Algorithms Implemented
=============================
1. TD-Q Learning Algorithm
   ------------------------
TD-Q Learning (Temporal Difference Q-learning) is an off-policy learning algorithm that analyzes Q-values for each state-action pair by using the maximum possible future rewards. This project employs the TDQLearner class from the SimpleAI library, which trains an agent by playing repeatedly against itself, where the agent initially plays against a random untrained agent, then it trains on itself, having made certain moves and updating its Q-values according to how favorable those moves were, and then the agent is put against a human.
2. SARSA Algorithm
   ---------------
SARSA is an on-policy reinforcement learning algorithm that updates Q-values on the basis of the actions chosen and the policy that is being applied. The SARSALearner class from SimpleAI is used to train an agent that learns to play Tic-Tac-Toe by following its current policy,in which the startegy is used same as TDQLearner, where Q-values are updated using state action pairs observed in the training.



######## How to Run
===================
->Train and test the TD-Q Learning agent:
python TDQLearner.py

->Train and test the SARSA agent:
python SARSALeraner.py



####### Performance Evaluation
==============================
The performance of the agents is evaluated using several key metrics, including the following:
1. Accumulated Rewards: The total rewards earned over multiple games, indicating how well the agent is performing based on its learned policy.
2. Known States: The total number of unique game state encountered by the agent after extended periods of continuous training, a larger set of known states shows a more comprehensive understanding of the game environment.
3. Temperature: The make_exponential_temperature function addresses this problem by gradually reducing exploration, thereby allowing the agent to rely on known strategies more and more as it gets better at the task. The PerformanceCounter class provided in SimpleAI serves to monitor and write down the relevant parameters and thus, in this case, illustrate the rate at which each agent is learning.



######### Results
=================
The performance of the agents is evaluated based on how many of games won, lost, or drawn. Graphs are generated to visualize the learning process and the accumulated rewards over time, which illustrate that the TD-Q Learning agent slightly outperforms the SARSA agent through repeated training episodes. It is also seen that both agents had performed equally, once also observed that SARSA ouperformed.

 **** output screenshots is in output_screenshots folder ****

######### Contributors
======================
- **Asma ul Husna** - Modified, implemented and compared the TD-Q Learning and SARSA algorithms within the Tic-Tac-Toe environment using the SimpleAI library.

- GitHub link - here is the link to the repository: https://github.com/Asma-ulhusna/tictactoe-using-reinforment-learning


########## References
=====================
1.SimpleAI- https://github.com/simpleai-team/simpleai.
