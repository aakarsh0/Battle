import pandas as pd
ground = []
def play():
    global ground
    L = len(ground[0])
    B = len(ground)
    print(pd.DataFrame(ground))

class Soldier:
    def __init__(self,team = None,position = None, energy = None,direction = None):
        self.team = team
        self.id = None
        self.energy = energy
        self.position = position
        self.direction = direction
        if(position==None):
            self.position = team + energy
    def info(self):
        return 'team: {}, position: {}, energy: {}'.format(self.team,self.position,self.energy)

s1 = Soldier(1,None,3)
print(s1.energy)
