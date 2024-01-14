from rich.console import Console
from rich.table import Table

from robot import *
from helper import *

#Settings
robots_count = 10
roster = [

robot(1234, 1, 2, 0.1),
robot(2345, 2, 1.7, .2),
robot(3456, 3, 1.55, .3),
robot(4567, 4, 1.4, .4),
robot(5678, 5, 1.25, .5),
robot(6789, 6, 1.1, .6),
robot(7890, 7, .95, .7),
robot(123, 8, .80, .8),
robot(234, 9, .65, .9),
robot(345, 10, .5, 1),

]

#main code
console1 = Console()

for bot in range(robots_count - len(roster)):
    team_num = int(input(f"Input team number for robot rank " + str(bot + 1) + ": "))
    new_cycle_multi = round(((3*(robots_count - bot))/(2*robots_count) + .5), 2)
    new_percent = round(((1/robots_count)*bot), 2)

    new_bot = robot(team_num, (bot + 1), new_cycle_multi, new_percent)
    console1.print(new_bot.box_print())
    roster.append(new_bot)

console1.print(full_comp_list(roster))
