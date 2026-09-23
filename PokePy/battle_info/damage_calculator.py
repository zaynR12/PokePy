from PokePy.models.pokemon import Pokemon
from PokePy.models.move import Move

def calculate_damage(attacking_pokemon: Pokemon, defending_pokemon: Pokemon, move: Move):
    base_damage = (
        (((2*attacking_pokemon.level / 5) + 2)
        * move.damage
        * attacking_pokemon.stats[0]
        / defending_pokemon.stats[1])
        / 50
    ) + 2
