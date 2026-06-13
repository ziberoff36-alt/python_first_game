from save import save
from support_functions import get_choice

def shop(player):
    while True:
        print(">>>Магазин<<<")
        print("Снаряжение:")
        print("1. Кристалл урона\n+10 урона, цена: 100 золотых")
        print("2. Доспех пехотинца\n+5 защиты, цена: 75  золотых")
        print("3. Эссенция жизни\n+20 максимального здоровья, цена 125 золотых")
        print("Расходники:")
        print("4. Зелье исцеления\n исцеляет на 30 здоровья в бою при применении, цена 50 золотых")
        print("5. Выход")
        shop_choice = get_choice(5)
        if shop_choice == 1:
            if any(item["name"] == "Кристалл урона" for item in player.inventory):
                print("У вас уже есть этот предмет!")
                continue
            if player.money >= 100:
                item = {"name": "Кристалл урона", "attack": 10, "count": 1}
                player.inventory.append(item)
                player.attack += item["attack"]
                player.money -= 100
                print("Вы успешно купили кристалл урона!")
            else:
                print("У вас недостаточно золота!")
                continue
        elif shop_choice == 2:
            if any(item["name"] == "Доспех пехотинца" for item in player.inventory):
                print("У вас уже есть этот предмет!")
                continue
            if player.money >= 75:
                item = {"name": "Доспех пехотинца", "defense": 5, "count": 1}
                player.inventory.append(item)
                player.defense += item["defense"]
                player.money -= 75
                print("Вы успешно купили доспех пехотинца!")
            else:
                print("У вас недостаточно золота!")
                continue
        elif shop_choice == 3:
            if any(item["name"] == "Эссенция жизни" for item in player.inventory):
                print("У вас уже есть этот предмет!")
                continue
            if player.money >= 125:
                item = {"name": "Эссенция жизни", "health": 20, "max_health": 20, "count": 1}
                player.inventory.append(item)
                player.health += item["health"]
                player.max_health += item["max_health"]
                player.money -= 125
                print("Вы успешно купили эссенцию жизни!")
            else:
                print("У вас недостаточно золота!")
                continue
        elif shop_choice == 4:
            if player.money >= 50:
                existing = next((item for item in player.inventory if item["name"] == "Зелье исцеления"),None)
                if existing is not None:
                    existing["count"] += 1
                else:
                    item = {"name": "Зелье исцеления", "health": 20, "count": 1}
                    player.inventory.append(item)
                player.money -= 50
        elif shop_choice == 5:
            print(f"До свидания, {player.name}!")
            save(player)
            break



