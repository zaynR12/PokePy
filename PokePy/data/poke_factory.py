from PokePy.data.poke_api_client import PokeApiClient
from PokePy.models.pokemon import Pokemon

class PokeFactory:

    def __init__(self):
        self.api_client = PokeApiClient()

    def build_pokemon(self, name:str):
        d = self.api_client.get_pokedic_stats(name)
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


        
