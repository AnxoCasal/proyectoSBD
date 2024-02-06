import requests
import random
import time
import os

class dnd_master:
    
    book = None
    
    def get_data(url):
        
        try:
            response = requests.get(url)
            response.raise_for_status()

            datos = response.json()
            return datos
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None

    def get_book(self):
        return self.book
    

    def dnd_minigame(self):
        
        monster_list = self.get_data("https://www.dnd5eapi.co/api/monsters")["results"]
        spell_list = self.get_data("https://www.dnd5eapi.co/api/spells")["results"]
        weapon_list = self.get_data("https://www.dnd5eapi.co/api/equipment")["results"]
        
        monster = random.choice(monster_list)
        spell = random.choice(spell_list)
        weapon = random.choice(weapon_list)
        
        monster_data = self.get_data(f"https://www.dnd5eapi.co/api/monsters/{monster['index']}")
        spell_data = self.get_data(f"https://www.dnd5eapi.co/api/spells/{spell['index']}")
        weapon_data = self.get_data(f"https://www.dnd5eapi.co/api/equipment/{weapon['index']}")
        
        monster_attacks = []
        
        for action in monster_data["actions"]:
            if "damage" in action.keys():
                monster_attacks.append(action["name"])
                
        
        if monster_list:
            
            start = f"You go out on your first adventure.\r\nTHE WORLD IS YOURS\r\n\r\nA {monster['name']} appears in front of you!\r\nIt's going to attack you!\r\n\r\nChoose your weapon!\r\n"
            spell = f"You cast \"{spell['name']}\"!"
            weapon = f"You look on your backpack and find a \"{weapon['name']}\"!"
                
            if "damage" in spell_data.keys():
                spell_res = "YOU KILL THE MONSTER!!!"
            else:
                spell_res = "That's a non damage spell\t0_0\r\n...\r\n"
                if monster_attacks:
                    spell_res += f"The {monster['name']} uses \"{random.choice(monster_attacks)}\" and destroys you!!!"
                else:
                    spell_res += f"The {monster['name']} is completly useless and escapes. You got lucky!!!"
            
            if "damage" in weapon_data.keys():
                weapon_res = "YOU KILL THE MONSTER!!!"
            else:
                weapon_res = "That's not a weapon\t0_0\r\n...\r\n"
                if monster_attacks:
                    weapon_res += f"The {monster['name']} uses \"{random.choice(monster_attacks)}\" and destroys you!!!"
                else:
                    weapon_res += f"The {monster['name']} is completly useless and escapes. You got lucky!!!"
                    
            history = {"start":start, "spell":spell, "weapon":weapon, "spell_res":spell_res, "weapon_res":weapon_res}
        
        self.book = history
        return history