from rich.table import Table
from robot import *

def full_comp_list(robot_list):

    prnt_table = Table(title="Full competition and attribute list")

    columns = ["name", "ranking", "percent", "ground_cap", "source_cap", "amp_cap", "speaker_cap", "trap_cap", "score_rating"]

    for column in columns:
        prnt_table.add_column(column)

    for bot in robot_list:
        prnt_table.add_row(*(bot.get_table_format()))

    return prnt_table