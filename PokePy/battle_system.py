from PokePy.trainer import *
from PokePy.pokemon import *

class BattleSystem():

    def __init__(self, Trainer1, Trainer2):
        self.Trainer1 = Trainer1
        self.Trainer2 = Trainer2
        self.CurrPokemonA = Trainer1.team[0] 
        self.CurrPokemonB = Trainer2.team[0]

    def player_turn(self, trainer, curr_pokemon, other_curr_pokemon):
            print(f"{trainer.name}'s turn!")
            print(f"{curr_pokemon.name} : {curr_pokemon.curr_hp} vs {other_curr_pokemon.name} : {other_curr_pokemon.curr_hp}")
            for move in curr_pokemon.moves:
                print(f"{move.name} ", end = '')
            print()
            inp = int(input(">>> "))

            print(f"{curr_pokemon.name} used {curr_pokemon.moves[inp].name}!")


    def battle_loop(self):
        
        print(f'!!! {self.Trainer1.name} IS BATTLIGN {self.Trainer2.name}')
        count = 0

        print(self.Trainer1.is_alive())
        print(self.Trainer2.is_alive())

        while self.Trainer1.is_alive() and self.Trainer2.is_alive():
            if count % 2==0:
                  
                self.player_turn(self.Trainer1, self.CurrPokemonA, self.CurrPokemonB)
            else:
                self.player_turn(self.Trainer2, self.CurrPokemonB, self.CurrPokemonA)
            count +=1 

        