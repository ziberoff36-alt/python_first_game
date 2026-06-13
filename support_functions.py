from save import save
from characters import Mage, Tank, Rogue

def get_choice(max_value):
    while True:
        try:
            choice = int(input("Ваш выбор:"))
        except ValueError:
            print("Выберите только из предложенных вариантов")
            continue
        if choice > max_value or choice < 1:
            print("Выберите только из предложенных вариантов")
            continue
        return choice
def use_consumable(player):
    while True:
        consumable = [item for item in player.inventory if item["type"] == "consumable"]
        if not consumable:
            print("У вас нет расходников!")
            break
        print(">>>Расходники<<<")
        for i, item in enumerate(consumable, start=1):
            print(f"{i}. {item['name']} ({item['count']} шт.) - восстанавливает {item['health']} HP.")
        print(f"{len(consumable) + 1}. Отмена")
        consumable_choice = get_choice(len(consumable) + 1)
        if consumable_choice == len(consumable) + 1:
            break
        else:
            chosen = consumable[consumable_choice - 1]
            player.health = min(player.max_health, player.health + chosen["health"])
            chosen["count"] -= 1
            if chosen["count"] == 0:
                player.inventory.remove(chosen)
            print(f"Вы использовали {chosen['name']}")
            break
def register_player():
    while True:
        name = input("Введите имя вашего персонажа:")
        if len(name) < 3:
            print("Ваше имя должно содержать не менее 3 символов")
            continue
        print("Отличное имя! Теперь выберите ему класс:", end="\n\n")
        print("1. Маг")
        print("Высокий урон, но малая выживаемость")
        print("Характеристики:")
        mage_registration = Mage(name)
        mage_registration.show_stats_registration()
        print("")
        print("2. Танк")
        print("Низкий урон, но крайне высокая выживаемость")
        print("Характеристики:")
        tank_registration = Tank(name)
        tank_registration.show_stats_registration()
        print("")
        print("3. Разбойник")
        print("Средние статы, но есть бонусные деньги на старте")
        print("Характеристики:")
        rogue_registration = Rogue(name)
        rogue_registration.show_stats_registration()
        registration_choice = get_choice(3)
        match registration_choice:
            case 1:
                player = Mage(name)
            case 2:
                player = Tank(name)
            case 3:
                player = Rogue(name)
        save(player)
        input("Поздравляем! Вы создали персонажа! Нажмите Enter, чтобы продолжить.")
        break