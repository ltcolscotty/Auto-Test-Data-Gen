from robot import *
import random

"""
input for match schedule should be a list of lists containing 6 teams in order of red1->blue3
eg.
[
[1234, 2345, 3456, 456, 567, 678],
[654, 234, 123, 3456, 3423, 1287],
[2345, 4532, 2321, 634, 667, 232],...
]
"""


class simulator:
    def __init__(self, roster, match_schedule):
        """roster, match_schedule"""
        self.roster = roster
        self.schedule = match_schedule

    def n_dice_six(n_num):
        """simulates n number 6 die rolls"""
        sum = 0
        for n in range(n_num):
            sum += random.randint(1, 6)
        return sum
    
    def run_sim(self, match):
        pass
    
    

    
