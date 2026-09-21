from BattleSystem import *
from Trainer import *
from Pokemon import *
from Move import *
from Menu import *





class main():
    running = True
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


    menu = Menu()

    while running:
        print("HOME MENU")
        print("1. build teams 2. battle")
        inp = input(">>> ")

        if inp == '1':
            menu.select_trainer_menu()



'''
    battle = BattleSystem(trainer1, trainer2)
    battle.battle_loop()
'''


main()