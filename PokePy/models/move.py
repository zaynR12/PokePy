class Move:
    def __init__(
        self,
        name: str,
        poke_type: str,
        damage: int,
        effect: str,
        chance: int,
        accuracy: int,
    ) -> None:
        self.name = name
        self.poke_type = poke_type
        self.damage = damage
        self.effect = effect
        self.chance = chance
        self.accuracy = accuracy
    