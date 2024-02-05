import requests
import random
import time
import os

def get_data(url):
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        datos = response.json()
        return datos
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None

def dnd_minigame():
    
    monster_list = get_data("https://www.dnd5eapi.co/api/monsters")["results"]
    spell_list = get_data("https://www.dnd5eapi.co/api/spells")["results"]
    weapon_list = get_data("https://www.dnd5eapi.co/api/equipment")["results"]
    
    monster = random.choice(monster_list)
    spell = random.choice(spell_list)
    weapon = random.choice(weapon_list)
    
    monster_data = get_data(f"https://www.dnd5eapi.co/api/monsters/{monster['index']}")
    spell_data = get_data(f"https://www.dnd5eapi.co/api/spells/{spell['index']}")
    weapon_data = get_data(f"https://www.dnd5eapi.co/api/equipment/{weapon['index']}")
    
    monster_attacks = []
    
    for action in monster_data["actions"]:
        if "damage" in action.keys():
            monster_attacks.append(action["name"])
            
    
    if monster_list:
        print(f"You go out on your first adventure. THE WORLD IS YOURS\r\n...\r\n")
        print(f"A {monster['name']} appears in front of you!\r\nIt's going to attack you!\r\n...\r\n")
        choice = input("Wanna choose magic or a weapon [m/w]\r\n")
        if choice == "m":
            print(f"You cast \"{spell['name']}\"!")
            if "damage" in spell_data.keys():
                print("YOU KILL THE MONSTER!!!")
            else:
                print("That's a non damage spell\t0_0\r\n...\r\n")
                if monster_attacks:
                    print(f"The {monster['name']} uses \"{random.choice(monster_attacks)}\" and destroys you!!!")
                else:
                    print(f"The {monster['name']} is completly useless and escapes. You got lucky!!!")
        else:
            print(f"You look on your backpack and find a \"{weapon['name']}\"!")
            if "damage" in weapon_data.keys():
                print("YOU KILL THE MONSTER!!!")
            else:
                print("That's not a weapon\t0_0\r\n...\r\n")
                if monster_attacks:
                    print(f"The {monster['name']} uses \"{random.choice(monster_attacks)}\" and destroys you!!!")
                else:
                    print(f"The {monster['name']} is completly useless and escapes. You got lucky!!!")
    
dnd_api()