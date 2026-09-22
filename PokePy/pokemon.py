from move import *

class Pokemon:
    def __init__(
            self,
            name: str,
            max_hp: int,
            attack: int,
            defense: int,
            special_attack:int,
            special_defense:int,
            poke_type: str,
            status: str,
    ) -> None:    
        self.name: str = name
        self.moves: list[Move] = []
        self.max_hp: int = max_hp
        self.curr_hp: int = max_hp
        self.stats: tuple[int, int, int, int] = (attack, defense, special_attack, special_defense)
        self.poke_type: str = poke_type
        self.status: str = status

    def __str__(self):
        return f"{self.name}, hp:{self.max_hp}"

    def is_fainted(self):
        return self.curr_hp < 0



    