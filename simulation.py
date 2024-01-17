from robot import *
from custom_exceptions import *
import random

"""
input for match schedule should be a list containing 6 teams in order of red1->blue3
eg.
[1234, 2345, 3456, 456, 567, 678]

"""


class simulator:
    def __init__(self, roster, match):
        """roster, match_schedule"""
        self.roster = roster
        self.schedule = match
        self.alliance1, self.alliance2 = self.create_alliances()
        

    def create_alliances(self):
        """creates alliances based on the match"""
        alliance1 = list()
        alliance2 = list()
        for n in range(1, 3):
            alliance1.append(self.find_bot(self.schedule[n]))
        for n in range (4, 6):
            alliance2.append(self.find_bot(self.schedule[n]))

        return alliance1, alliance2


    def find_bot(self, target_name):
        for bot in self.roster:
            if bot.name == target_name:
                return bot
            else:
                raise BotNotFound
                


    def n_dice_six(n_num):
        """simulates n number 6 die rolls"""
        sum = 0
        for n in range(n_num):
            sum += random.randint(1, 6)
        return sum
    

    def run_sim(self, match):
        """return format:
        team, showed_up, 
        """
        performance_dict = {}

        for robot in match:
            performance_dict[robot] = list(robot.name)

            self.sim_show(robot)
            performance_dict[robot].append(self.show())
            if self.show():
                pass
            else:
                pass

    
    def defense_sim(self, robot):
        """Simulates defense star rating"""
        dr = self.n_dice_six(1)

        if (robot.percent > .75) or (robot.percent < .25):
            dr -= 3
            if dr <= 0:
                return 0
            else:
                return dr
            
        else:
            if dr >= 5:
                return 3
            elif dr >= 3:
                return 2
            elif dr == 2:
                return 1
            else:
                return 0


    def auto_sim(self, robot):
        """[scored, left_start, center_pickup]"""
        scored = 0


    def tele_sim(self, robot):
        """[]"""


    def penalty_sim(self, robot):
        """[]"""


    def sim_show(self, robot):
        """Simulates if the robot showed up at all"""
        dr = self.n_dice_six(3)

        if (robot.percent <= .2) and (dr >= 17):
            self.show = False

        elif (dr >= 16):
            self.show = False
        
        else:
            self.show = True


    


    
