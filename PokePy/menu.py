from trainer import *

class Menu():

    def __init__(self):
        pass

    def select_trainer_menu(self):
        print("SELECT TRAINER MENU:")
        print(*Trainer.all_trainers_dic.values())
        print("Or C to create new")
        inp = input(">>> ")
        self.team_build_menu(Trainer.all_trainers_dic[int(inp)])




    def team_build_menu(self, trainer):
        print("TEAM BUILD MENU")
        print("curr:")
        print(*trainer.team)
        p = input("Give pokemon name e.g. charmander")
        trainer.add_pokemon(p)
        print(*trainer.team)

