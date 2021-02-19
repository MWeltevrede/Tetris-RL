# Tetris-RL
This project will implement a deep reinforcement learning agent for Tetris based on ideas from Hierarchical Reinforcement Learning.
The main hypothesis is that Tetris is incredibly difficult to solve due to the sparsity of rewards and the fact that almost all single actions (move left, move right, or rotations) are perfectly reversible. 

To try and overcome this, I will train a hierarchy of agents: a manager and a worker. The manager will decide where blocks end up on the board (horizontal position and orientation) and the worker will be tasked with getting the block there. 



## Dependencies
This project uses the pyTetris engine from [here](https://github.com/hrpan/pyTetris).


## Literature
1. [Playing Tetris with Deep Reinforcement Learning](http://cs231n.stanford.edu/reports/2016/pdfs/121_Report.pdf) (A report on DQN applied to Tetris)
2. [Learn to Play Tetris with Deep Reinforcement Learning](https://openreview.net/pdf/a058132ebf2949cfe77aba52c35876932fc169d2.pdf) (An article showing the difficulties of solving the original Tetris environment. They instead solve a simplified version of the game with modified state and action space)
3. [Deep Q-learning for playing Tetris](https://github.com/uvipen/Tetris-deep-Q-learning-pytorch) (A repository on which the solution of 2. is based)
4. [Learning to play Tetris with Monte Carlo Tree Search and Temporal Difference Learning](https://github.com/hrpan/tetris_mcts) (A repository using MCTS rather than other model-free RL approaches to avoid having to use heuristics)
