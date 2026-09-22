from trainer import Trainer
from pokemon import Pokemon
from move import Move



def setup_test_data():
    print("test ----------------------------------------------------------")
    trainer1 = Trainer("Ash")
    trainer2 = Trainer("Cynthia")

    pikachu = Pokemon("Pikachu", 100, 50, 50, 50, 50, "electric", None)
    garchomp = Pokemon("Garchomp", 100, 50, 50, 50, 50, "dragon", None)

    trainer1.team.append(pikachu)
    trainer2.team.append(garchomp)

    thunderbolt = Move("Thunderbolt", "electric", 50, None, 0, 100)
    tackle = Move("Tackle", "normal", 50, None, 0, 100)
    pikachu.moves.append(thunderbolt)
    pikachu.moves.append(tackle)

    garchomp.moves.append(tackle)

    trainer1.add_pokemon("charmander")

    print(*trainer1.team)



