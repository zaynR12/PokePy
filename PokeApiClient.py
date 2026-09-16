import requests

class PokeApiClient():
    def __init__(self):

        pass



    def fetch_pokedic(self, name:str):
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = requests.get(url)

        if response.ok:
            poke_dic = response.json()
            return poke_dic
        else:
            print("Error! Incorrect Pokemon name!")


    def get_pokedic_stats(self, name: str):
        poke_dic = self.fetch_pokedic(name)
        #id = poke_dic[id]

        poke_stat_dic = {
        "base_hp"     : poke_dic["stats"][0]["base_stat"],
        "base_attack" : poke_dic["stats"][1]["base_stat"],
        "base_def"    : poke_dic["stats"][2]["base_stat"],
        "base_sp_attack" : poke_dic["stats"][3]["base_stat"],
        "base_sp_def"    : poke_dic["stats"][4]["base_stat"],
        "base_speed"     : poke_dic["stats"][5]["base_stat"]
        }

        print("DEBUGGING LINE IN POKEAPICLIENT POKESTATDIC")
        for k,v in poke_stat_dic.items():
            print(k, v)
        print("fin debug-----------------------------------")
        return poke_stat_dic







'''
API = PokeApiClient()

API.get_pokemon("charmander")
'''

