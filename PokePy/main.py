from PokePy.data.test_data import setup_test_data
from ui.menu import Menu
from PokePy.battle_info.battle_system import BattleSystem



def main():
    trainer1, trainer2 = setup_test_data()

    menu = Menu()
    running = True
    while running:
        print("HOME MENU")
        print("1. build teams 2. battle")
        inp = input(">>> ")

        if inp == '1':
            menu.select_trainer_menu()
        if inp =='2':
            battle = BattleSystem(trainer1, trainer2)
            battle.battle_loop()
        if inp == '3':
             exit()
             

if __name__ == '__main__':
    main()