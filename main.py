from rich.console import Console
from rich.table import Table

from robot import *
from helper import *
from simulation import *

#Settings
robots_count = 10
roster = [

robot(1234, 1, 0.1, preset_bool=1),
robot(2345, 2, .2, preset_bool=1),
robot(3456, 3, .3, preset_bool=1),
robot(4567, 4, .4, preset_bool=1),
robot(5678, 5, .5, preset_bool=1),
robot(6789, 6, .6, preset_bool=1),
robot(7890, 7, .7, preset_bool=1),
robot(123, 8, .8, preset_bool=1),
robot(234, 9, .9, preset_bool=1),
robot(345, 10, 1, preset_bool=1),

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


