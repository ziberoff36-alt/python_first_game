from characters import *

def player_creation():
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
        break