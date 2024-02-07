import requests
import random
import time
import os

class dnd_master:
    
    book = None

    @staticmethod
    def get_data(url):
        
        try:
            response = requests.get(url)
            response.raise_for_status()

            datos = response.json()
            return datos
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None

    @staticmethod
    def get_book():
        return dnd_master.book
    

    @staticmethod
    def dnd_minigame():
        
        monster_list = dnd_master.get_data("https://www.dnd5eapi.co/api/monsters")["results"]
        spell_list = dnd_master.get_data("https://www.dnd5eapi.co/api/spells")["results"]
        weapon_list = dnd_master.get_data("https://www.dnd5eapi.co/api/equipment")["results"]
        
        monster = random.choice(monster_list)
        spell = random.choice(spell_list)
        weapon = random.choice(weapon_list)
        
        monster_data = dnd_master.get_data(f"https://www.dnd5eapi.co/api/monsters/{monster['index']}")
        spell_data = dnd_master.get_data(f"https://www.dnd5eapi.co/api/spells/{spell['index']}")
        weapon_data = dnd_master.get_data(f"https://www.dnd5eapi.co/api/equipment/{weapon['index']}")
        
        monster_attacks = []
        
        for action in monster_data["actions"]:
            if "damage" in action.keys():
                monster_attacks.append(action["name"])
                
        
        if monster_list:
            
            start = f"You go out on your first adventure...\r\nTHE WORLD IS YOURS!\r\n\r\nA {monster['name']} appears in front of you!\r\nIt's going to attack you!\r\n\r\nFast! Choose your weapon!\r\n"
            spell = f"You cast \"{spell['name']}\"!\r\n"
            weapon = f"You look on your backpack and find a \"{weapon['name']}\"!\r\n"
                
            if "damage" in spell_data.keys():
                spell += f"YOU KILL THE {monster['name'].upper()}!!!"
            else:
                spell += "That's a non damage spell\t0_0\r\n...\r\n"
                if monster_attacks:
                    spell += f"The {monster['name']} uses \"{random.choice(monster_attacks)}\" and destroys you!!!"
                else:
                    spell += f"The {monster['name']} is completly useless and escapes. You got lucky!!!"
            
            if "damage" in weapon_data.keys():
                weapon += f"YOU KILL THE {monster['name'].upper()}!!!"
            else:
                weapon += "That's not a weapon\t0_0\r\n...\r\n"
                if monster_attacks:
                    weapon += f"The {monster['name']} uses \"{random.choice(monster_attacks)}\" and destroys you!!!"
                else:
                    weapon += f"The {monster['name']} is completly useless and escapes. You got lucky!!!"
                    
            history = {"start":start, "spell":spell, "weapon":weapon}
        
        dnd_master.book = history
        return history