from Pokemon import *
from PokeFactory import *

class Trainer():

    def __init__(self, name):
        self.name = name
        self.team = []

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