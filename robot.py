from rich.table import Table

class robot:
    def __init__(self, team_number, ranking, cycle_factor, percent, parameters=None, preset_bool=0):
        """
        Basic input format: team_number, ranking, cycle_factor, percent
        preset_bool = 0: default setting, no presets
        preset_bool = 1: set to true
        preset_bool = 2: set to false
        """

        if parameters == None:

            self.preset_bool = preset_bool

            #Default sets
            self.name = str(team_number) #Name of team
            self.ranking = int(ranking) #Ranking in hirearchy - int
            self.cycle_factor = float(cycle_factor) #Cycle speed multiplier - entered as a float
            self.percent = float(percent) #reverse percentile sort of thing - entered as a float (lower = better team)
            
            #Autoset and calculated traits, these change from year to year
            self.grnd_pu_cap = self.prompt_bool(upper=.5, lower=.3, measure_name="ground pickup capable")
            self.srce_pu_cap = self.prompt_bool(upper=.6, lower=.1, measure_name="source pickup capable")
            self.amp_cap = self.prompt_bool(upper=.6, lower=.2, measure_name="amp capable")
            self.spkr_cap = self.prompt_bool(upper=.4, lower=.2, measure_name="speaker capable")
        else:
            self.name = parameters["name"]
            self.ranking = parameters["ranking"]
            self.cycle_factor = parameters["cycle_multi"]
            self.percent = parameters["percent"]
            self.grnd_pu_cap = parameters["ground_cap"]
            self.srce_pu_cap = parameters["source_cap"]
            self.amp_cap = parameters["amp_cap"]
            self.spkr_cap = parameters["speaker_cap"]


    def __str__(self):
        return "Name: " + self.name
            

    def box_print(self):
        """Rich formatting"""
        columns = ["name", "ranking", "cycle_multi", "percent", "ground_cap", "soource_cap", "amp_cap", "speaker_cap"]
        row = self.get_table_format()
        prnt_table = Table(title="Robot: " + self.name)

        for column in columns:
            prnt_table.add_column(column)
        
        prnt_table.add_row(*row)
        
        return prnt_table
        
    
    def export_parameters(self):
        """returns dictionary containing all set robot parameters"""
        exp_param = {
            "name": self.name,
            "ranking": self.ranking,
            "cycle_multi": self.cycle_factor,
            "percent": self.percent,
            "ground_cap": self.grnd_pu_cap,
            "source_cap": self.srce_pu_cap,
            "amp_cap": self.amp_cap,
            "speaker_cap": self.spkr_cap
        }
        
        return exp_param


    def get_table_format(self):
        """returns list with parameters of robot"""
        tbl_frm = [self.name, self.ranking, self.cycle_factor, self.percent, self.grnd_pu_cap, self.srce_pu_cap, self.amp_cap, self.spkr_cap]
        return map(str, tbl_frm)
    

    def prompt_bool(self, upper=0, lower=1, measure_name=""):
        """
        enter upper and lower in float format, they should all be less than 1
        upper -> Above this percent robot will have trait
        lower -> Below this percent robot will not have trait
        Anything in between will be prompted
        """

        if self.percent <= upper:
            return True
        elif self.percent >= (1-lower):
            return False
        else:
            if self.preset_bool == 1:
                return True
            elif self.preset_bool == 2:
                return False
            else:
                print(f"The measure " + measure_name + " needs to be set manually")
                answer = False
                while not answer:
                    determine = input(f"Entry requested for " + self.name + " for " + measure_name + ". Enter [Y/N]: ")
                    if determine.casefold() == "y".casefold():
                        return True
                    elif determine.casefold() == "n".casefold():
                        return False
                    else:
                        print("Invalid input, try again")




    
