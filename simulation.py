from robot import *
import random

class simulator:
    def __init__(self, roster):
        self.roster = roster

    def n_dice_six(n_num):
        sum = 0
        for n in range(n_num):
            sum += random.randint(1, 6)
        return sum
    
    def run_sim(self):
        pass
    

    
