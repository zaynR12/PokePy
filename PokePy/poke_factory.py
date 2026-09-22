from poke_api_client import *
from pokemon import *

class PokeFactory():

    def __init__(self):
        pass

    def buildPokeObject(self, name:str):
        d = PokeApiClient().get_pokedic_stats(name)
        p = Pokemon(
            name,
            d["base_hp"],
            d["base_attack"],
            d["base_def"],
            d["base_sp_attack"],
            d["base_sp_def"],
            None,
            None
        )
        return p


        
