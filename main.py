from rich.console import Console
from rich.table import Table

from robot import *
from helper import *
from simulation import *

#Settings
robots_count = 16
roster = [
robot(2345, 1, .1, preset_bool=1),
robot(3456, 2, .15, preset_bool=1),
robot(4567, 3, .2, preset_bool=1),
robot(5678, 4, .25, preset_bool=1),
robot(6789, 5, .3, preset_bool=1),
robot(7890, 6, .35, preset_bool=1),
robot(123, 7, .4, preset_bool=1),
robot(234, 8, .45, preset_bool=1),
robot(3451, 9, .5, preset_bool=1),
robot(3452, 10, .55, preset_bool=1),
robot(3453, 11, .6, preset_bool=1),
robot(3454, 12, .65, preset_bool=1),
robot(3455, 13, .7, preset_bool=1),
robot(3457, 14, .75, preset_bool=1),
robot(3458, 15, .8, preset_bool=1),
robot(3459, 16, .85, preset_bool=1),
robot(3450, 17, .9, preset_bool=1),
robot(3444, 18, .95, preset_bool=1),
robot(3445, 19, 1, preset_bool=1),

]


#main code
console1 = Console()

#figures out how many spots need to be filled based on preset roster then generates stats for them
for bot in range(robots_count - len(roster)):
    team_num = int(input(f"Input team number for robot rank " + str(bot + 1) + ": "))
    new_percent = round(((1/robots_count)*bot), 2)
    new_bot = robot(team_num, (bot + 1), new_percent)
    
    roster.append(new_bot) #add new bot to roster

console1.print(full_comp_list(roster))


