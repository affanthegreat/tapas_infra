from machine_learning.tapas_framework.core import *


class TapasBaseClass:
    def __init__(self) -> None:
        self.model = Model("base_weights/","SQA")
        self.table = [['Pos', 'No', 'Driver', 'Team', 'Laps', 'Time/Retired', 'Grid', 'Points'],
         ['1', '32', 'Patrick Carpentier', "Team Player's", '87', '1:48:11.023', '1', '22'],
         ['2', '1', 'Bruno Junqueira', 'Newman/Haas Racing', '87', '+0.8 secs', '2', '17'],
         ['3', '3', 'Paul Tracy', "Team Player's", '87', '+28.6 secs', '3', '14'],
         ['4', '9', 'Michel Jourdain, Jr.', 'Team Rahal', '87', '+40.8 secs', '13', '12'],
         ['5', '34', 'Mario Haberfeld', 'Mi-Jack Conquest Racing', '87', '+42.1 secs', '6', '10'],
         ['6', '20', 'Oriol Servia', 'Patrick Racing', '87', '+1:00.2', '10', '8'],
         ['7', '51', 'Adrian Fernandez', 'Fernandez Racing', '87', '+1:01.4', '5', '6'],
         ['8', '12', 'Jimmy Vasser', 'American Spirit Team Johansson', '87', '+1:01.8', '8', '5'],
         ['9', '7', 'Tiago Monteiro', 'Fittipaldi-Dingman Racing', '86', '+ 1 Lap', '15', '4'],
         ['10', '55', 'Mario Dominguez', 'Herdez Competition', '86', '+ 1 Lap', '11', '3'],
         ['11', '27', 'Bryan Herta', 'PK Racing', '86', '+ 1 Lap', '12', '2'],
         ['12', '31', 'Ryan Hunter-Reay', 'American Spirit Team Johansson', '86', '+ 1 Lap', '17', '1'],
         ['13', '19', 'Joel Camathias', 'Dale Coyne Racing', '85', '+ 2 Laps', '18', '0'],
         ['14', '33', 'Alex Tagliani', 'Rocketsports Racing', '85', '+ 2 Laps', '14', '0'],
         ['15', '4', 'Roberto Moreno', 'Herdez Competition', '85', '+ 2 Laps', '9', '0'],
         ['16', '11', 'Geoff Boss', 'Dale Coyne Racing', '83', 'Mechanical', '19', '0'],
         ['17', '2', 'Sebastien Bourdais', 'Newman/Haas Racing', '77', 'Mechanical', '4', '0'],
         ['18', '15', 'Darren Manning', 'Walker Racing', '12', 'Mechanical', '7', '0'],
         ['19', '5', 'Rodolfo Lavin', 'Walker Racing', '10', 'Mechanical', '16', '0']]

    def set_table(self, table):
        self.table = table

    def ask(self,query):
        print(query)
        return self.model(self.table, [query])
