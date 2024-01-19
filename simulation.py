from robot import *
from custom_exceptions import *
import random

"""
Input for match schedule should be a list containing 6 teams in order of red1->blue3
eg.
[1234, 2345, 3456, 456, 567, 678]

Simulates ONE match
"""

"""Object structuring


"""


class simulator:
    def __init__(self, roster, match):
        """roster, match_schedule"""
        self.roster = roster
        self.schedule = match
        self.alliance1, self.alliance2 = self.create_alliances()
        

    def create_alliances(self):
        """creates alliances based on the match"""
        alliance1 = {}
        alliance2 = {}

        alliance1robots = list()
        alliance2robots = list()
        for n in range(1, 3):
            alliance1robots.append(self.find_bot(self.schedule[n]))
        for n in range (4, 6):
            alliance2robots.append(self.find_bot(self.schedule[n]))

        alliance1["robots"] = alliance1robots
        alliance2["robots"] = alliance2robots

        return alliance1, alliance2


    def find_bot(self, target_name):
        """takes bot name and returns bot object"""
        for bot in self.roster:
            if bot.name == target_name:
                return bot
            else:
                raise BotNotFound
                

    def n_dice_six(n_num):
        """simulates n number 6 die rolls, returns sum"""
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
        left_start = False
        center_pickup = False

        #sim auto scoring
        dr = self.n_dice_six(1)

        if robot.percent >= .8:
            scored = 0
        elif robot.percent <= .3 and dr >= 5:
            scored = 1
        elif robot.percent <= .3 and dr < 5:
            scored = 2
        elif dr >= 5:
            scored = 2
        elif dr >= 2:
            scored = 1
        else:
            scored = 0

        
        # sim left start
        dr = self.n_dice_six(1)
        if scored > 1 or robot.percent <= .2 or dr > 1:
            left_start = True

        #sim center pickup
        if scored >= 2 and robot.grnd_pu_cap:
            center_pickup = True

        return [scored, left_start, center_pickup]


    def tele_sim_bot(self, robot):
        """[speaker_score, amp_score, coopertition, fouls, disable_status]"""


    def tele_sim_alliance(self, alliance):
        """[amp_periods]"""
        coopertition_status = False
        total_rating = 0

        #get scoring rating
        for robot in alliance:
            total_rating += robot.score_rating

        amp_score = (2 * self.amp_period_count(total_rating))
        

    def sim_speaker(self, robot):
        """simulates speaker scoring for one robot"""
        dr = self.n_dice_six(2)
        if robot.percent <= .5:
            return dr - 3
        else:
            return dr/2


    


    def amp_period_count(self, total):
        """returns period count"""
        if total == 0:
            return 0
        elif total <= 3:
            return 1
        elif total <= 6:
            return 2
        elif total <= 9:
            return 3
        elif total <= 11:
            return 4
        else:
            return 5


    def penalty_sim(self, robot):
        """[fouls]"""

        #sim dr
        dr = self.n_dice_six(3)
        if robot.percent < .5:
            fouls = dr - 14
        else:
            fouls = dr - 12
        
        #filter to prevent negatives
        if fouls >= 0:
            return fouls
        else:
            return 0


    def sim_show(self, robot):
        """Simulates if the robot showed up at all"""
        dr = self.n_dice_six(3)

        if (robot.percent <= .2) and (dr >= 17):
            self.show = False

        elif (dr >= 16):
            self.show = False
        
        else:
            self.show = True


    


    
