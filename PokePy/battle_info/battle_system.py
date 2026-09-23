from PokePy.models.trainer import Trainer
from PokePy.models.pokemon import Pokemon
class BattleSystem():

    def __init__(self, Trainer1: Trainer, Trainer2: Trainer):
        self.Trainer1 = Trainer1
        self.Trainer2 = Trainer2
        
        self.CurrPokemonA = Trainer1.team[0] 
        self.CurrPokemonB = Trainer2.team[0]

    def player_turn(self, trainer: Trainer, curr_pokemon: Pokemon, other_curr_pokemon: Pokemon):
            print(f"{trainer.name}'s turn!")
            print(f"{curr_pokemon.name} : {curr_pokemon.curr_hp} vs {other_curr_pokemon.name} : {other_curr_pokemon.curr_hp}")
            for move in curr_pokemon.moves:
                n=0
                print(f"n.{move.name} ", end = '')
            print()
            inp = int(input(">>> "))

            print(f"{curr_pokemon.name} used {curr_pokemon.moves[inp].name}!")
            #calculate damage!
            temp_damage = 50
            #apply damage!
            #damage happened!


    def battle_loop(self):
        
        print(f'!!! {self.Trainer1.name} IS BATTLIGN {self.Trainer2.name}')
        count = 0


        while self.Trainer1.is_alive() and self.Trainer2.is_alive():
            print(f"TURN: {count}")
            if count % 2==0:
                  
                self.player_turn(self.Trainer1, self.CurrPokemonA, self.CurrPokemonB)
            else:
                self.player_turn(self.Trainer2, self.CurrPokemonB, self.CurrPokemonA)
            count +=1 

        