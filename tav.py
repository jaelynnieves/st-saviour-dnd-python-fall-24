import random
from draw import draw_d20

class Tav:
    def __init__(self, name: str, role:str):
        self.name = name
        self.role = role 

        self.level = 1

        self.strength = 0
        self.wisdom = 0
        self.charisma = 0 
        self.intelligence = 0
        self.constitution = 0 
        self.dexterity = 0 

        self.assign_stats()



    def print_character_sheet(self):
        print('name: '  + self.name)
        print('role: '  + self.role)
        print('level: ' + str(self.level))
       
        print('------------------')
        
        print('strength: '     + str(self.strength))
        print('intelligence: ' + str(self.intelligence))
        print('charisma '      + str(self.charisma))
        print('wisdom   '      + str(self.wisdom))
        print('dextirity '     + str(self.dexterity))
        print('constitution'   + str(self.constitution))
        print()

    def assign_stats(self):
        stats = [15, 14, 13, 12, 10, 8]
        random.shuffle(stats)
       
        self.strength     = stats[0]
        self.dexterity    = stats[1]
        self.intelligence = stats[2]
        self.charisma     = stats[3]
        self.constitution = stats[4]
        self.wisdom       = stats[5]

    def roll() -> int:
        roll= random.randint(1, 20)
        draw_d20(roll)
        return roll 

