from characters import WeakGoblin, Goblin
from battle import battle
from shop import shop
from save import save, restore, reset, load
from support_functions import get_choice, register_player

player = None
print('Добро пожаловать в мир RPG!')
while True:
    print("   >>>>Меню выбора<<<<")
    print('Выберите "1", чтобы создать нового персонажа.')
    print('Выберите "2", чтобы играть.')
    print('Выберите "3", чтобы покинуть игру.')
    print('Выберите "4", чтобы удалить сохранение.')
    choice = get_choice(4)
    if choice == 4:
        reset()
        continue
    elif choice == 3:
        print("До свидания!")
        if player is not None:
            save(player)
        break
    elif choice == 1:
        player = register_player()
    elif choice == 2:
        if load() is None:
            print("Сохранение не найдено! Сначала создайте персонажа.")
            continue
        player = restore()
        while True:
            print(">>>>Меню<<<<")
            print("1. Испытания")
            print("2. Магазин")
            print("3. Характеристики")
            print("4. Выход")
            menu_choice = get_choice(4)
            if menu_choice == 1:
                print("Выберите сложность:\n1. Легкая\n2. Нормальная")
                dungeon_choice = get_choice(2)
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