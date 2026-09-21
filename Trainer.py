from Pokemon import *
from PokeFactory import *

class Trainer():

    all_trainers = []
    all_trainers_dic = {}
    count = 0

    def __init__(self, name):
        self.name = name
        self.team = []
        Trainer.all_trainers.append(self)
        Trainer.count += 1
        Trainer.all_trainers_dic[Trainer.count] = self

    def __str__(self):
        return f"{self.name}"

    def is_alive(self):
        for pokemon in self.team:
            if not pokemon.is_fainted():
                return True
        return False

    def add_pokemon(self, name: str):
        fac = PokeFactory()
        p = fac.buildPokeObject(name)
        print(p)
        self.team.append(p)
                
    pass