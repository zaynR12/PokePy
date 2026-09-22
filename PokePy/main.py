from test_data import setup_test_data
from menu import Menu


def main():
    setup_test_data()

    menu = Menu()
    running = True
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

if __name__ == '__main__':
    main()