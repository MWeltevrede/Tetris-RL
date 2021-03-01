from pyTetris import Tetris as T

class Tetris(T):
    """
    Description:
        A simple OpenAI Gym style wrapper for the pyTetris environment
    
    Source:
        https://github.com/hrpan/pyTetris
        
    Actions:
        0 : Rotate counter-clockwise
        1 : Rotate clockwise
        2 : Move left
        3 : Move down
        4 : Move right
        5 : Hard drop
        6 : pass
    
    Observation:
        Returns the current state of the board
        
    Reward:
        Returns the score following the official Tetris guideline
    """
    def __init__(self, boardsize):
        actions_per_drop = 1
        tetris_scoring = 0     # Scoring system used by Tetris (0: official guideline, 1: line clears)
        tetris_randomizer = 0   # Queue randomizer used by Tetris (0: bag, 1: uniform)
        super().__init__(boardsize, actions_per_drop, tetris_scoring, tetris_randomizer)
        
    def step(self, action):
        self.play(action)
        
        return self.getState(), self.score, self.end
    
    def reset(self):
        super().reset()
        
        return self.getState()