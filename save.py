import json
from characters import *
import os

def save(player):
    data = {
        "name": player.name,
        "level": player.level,
        "money": player.money,
        "health": player.health,
        "max_health": player.max_health,
        "attack": player.attack,
        "defense": player.defense,
        "exp": player.exp,
        "exp_needed": player.exp_needed,
        "character_class": player.character_class
    }
    with open("save.json", "w") as file:
        json.dump(data, file)
def load():
    try:
        with open("save.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None
def restore():
    classes = {
        "Маг": Mage,
        "Танк": Tank,
        "Разбойник": Rogue
    }
    save_data = load()
    player = classes[save_data["character_class"]](save_data["name"])
    player.health = save_data["health"]
    player.max_health = save_data["max_health"]
    player.exp = save_data["exp"]
    player.exp_needed = save_data["exp_needed"]
    player.level = save_data["level"]
    player.money = save_data["money"]
    player.attack = save_data["attack"]
    player.defense = save_data["defense"]
    return player
def reset():
    if os.path.exists("save.json"):
        os.remove("save.json")
        print("Сохранение успешно удалено.")
    else:
        print("Сохранение не найдено")