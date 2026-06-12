from characters import Mage, Tank, Rogue, WeakGoblin, Goblin
from battle import battle
from shop import shop
from save import save, restore, reset

player = None
print('Добро пожаловать в мир RPG!')
while True:
    print("   >>>>Меню выбора<<<<")
    print('Выберите "1", чтобы создать нового персонажа.')
    print('Выберите "2", чтобы играть.')
    print('Выберите "3", чтобы покинуть игру.')
    print('Выберите "4", чтобы удалить сохранение.')
    try:
        choice = int(input("Ваш выбор:"))
    except ValueError:
        print("Введите цифру, а не слово!")
        continue
    if choice > 4 or choice < 1:
        print("Выберите только из предложенных вариантов")
        continue
    if choice == 4:
        reset()
        continue
    elif choice == 3:
        print("До свидания!")
        if player is not None:
            save(player)
        break
    elif choice == 1:
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
        try:
            registration_choice = int(input("Ваш выбор:"))
        except ValueError:
            print("Выберите номер класса")
            continue
        if registration_choice > 3 or registration_choice < 1:
            print("Введите предложенный номер класса!")
            continue
        match registration_choice:
            case 1:
                player = Mage(name)
            case 2:
                player = Tank(name)
            case 3:
                player = Rogue(name)
        save(player)
        input("Поздравляем! Вы создали персонажа! Нажмите Enter, чтобы продолжить.")
    elif choice == 2:
        if player is None:
            print("Сохранение не найдено! Сначала создайте персонажа.")
            continue
        player = restore()

        while True:
            print(">>>>Меню<<<<")
            print("1. Испытания")
            print("2. Магазин")
            print("3. Характеристики")
            print("4. Выход")
            try:
                menu_choice = int(input("Ваш выбор:"))
            except ValueError:
                print("Выберите только из предложенных вариантов")
                continue
            if menu_choice > 4 or menu_choice < 1:
                print("Выберите только из предложенных вариантов")
                continue

            if menu_choice == 1:
                print("Выберите сложность:\n1. Легкая\n2. Нормальная")
                try:
                    dungeon_choice = int(input("Ваш выбор:"))
                except ValueError:
                    print("Выберите только из предложенных вариантов")
                    continue
                if dungeon_choice > 2 or dungeon_choice < 1:
                    print("Выберите только из предложенных вариантов")
                    continue
                if dungeon_choice == 1:
                    weak_goblin = WeakGoblin()
                    battle(player, weak_goblin)
                elif dungeon_choice == 2:
                    ordinary_goblin = Goblin()
                    battle(player, ordinary_goblin)

            elif menu_choice == 2:
                shop(player)

            elif menu_choice == 3:
                player.show_stats()

            elif menu_choice == 4:
                print(f"До свидания, {player.name}")
                break
    else:
        print("Такой опции нет!")
        continue