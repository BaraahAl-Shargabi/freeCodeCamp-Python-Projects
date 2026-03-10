** start of main.py **

from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self):
        selected_move = random.choice(self.moves)
        new_x = self.position[0] + selected_move[0]
        new_y = self.position[1] + selected_move[1]
        self.position = (new_x, new_y)
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(1,0) , (-1,0), (0,1), (0,-1)]
        
    def level_up(self):
        self.moves.extend([(1,1), (-1,1), (1,-1), (-1,-1)])




** end of main.py **

