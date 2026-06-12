from save import save
def shop(player):
    while True:
        print(">>>Магазин<<<")
        print("1. Кристалл урона\n+10 урона, цена: 100 золотых")
        print("2. Доспех пехотинца\n+5 защиты, цена: 75  золотых")
        print("3. Эссенция жизни\n+20 здоровья, цена 125 золотых")
        print("4. Выход")
        try:
            shop_choice = int(input("Ваш выбор:"))
        except ValueError:
            print("Выберите только из предложенных вариантов")
            continue
        if shop_choice > 4 or shop_choice < 1:
            print("Выберите только из предложенных вариантов")
            continue

        if shop_choice == 1:
            if player.money >= 100:
                player.attack += 10
                player.money -= 100
                print("Вы успешно купили кристалл урона!")
            else:
                print("У вас недостаточно золота!")
                continue

        elif shop_choice == 2:
            if player.money >= 75:
                player.defense += 5
                player.money -= 75
                print("Вы успешно купили доспех пехотинца!")
            else:
                print("У вас недостаточно золота!")
                continue

        elif shop_choice == 3:
            if player.money >= 125:
                player.max_health += 20
                player.health += 20
                player.money -= 125
                print("Вы успешно купили эссенцию жизни!")
            else:
                print("У вас недостаточно золота!")
                continue

        elif shop_choice == 4:
            print(f"До свидания, {player.name}!")
            save(player)
            break



