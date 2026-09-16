class Pokemon():

    def __init__(self, name, max_hp, attack, defense, special_attack, special_defense, type, status):
        self.name: str = name
        self.moves = []
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.stats = (attack, defense, special_attack, special_defense)
        self.type = type
        self.status = status

    def __str__(self):
        return f"{self.name}, hp:{self.max_hp}"

    def is_fainted(self):
        return self.curr_hp < 0



    