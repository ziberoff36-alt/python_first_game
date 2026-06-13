from save import save
import random
def start_battle(player, enemy):
    print("Начинается бой!")
    print(f"{player.name} (HP: {player.health}) vs {enemy.name} (HP: {enemy.health})")
def attack_battle(attacker, defender):
    damage = max(attacker.attack - defender.defense, 1)
    random_attack = random.randint(1, 100)
    if random_attack <= 20:
        damage *= 2
        print(f"{attacker.name} наносит критический удар!")
        defender.health -= damage
        print(f"{attacker.name} наносит {damage} урона! У {defender.name} осталось {defender.health} HP")
    elif 20 < random_attack <= 30:
        print(f"{attacker.name} промахнулся(-ась)!")
    else:
        defender.health -= damage
        print(f"{attacker.name} наносит {damage} урона! У {defender.name} осталось {defender.health} HP")
def defense_battle(defender, attacker):
    damage = max(attacker.attack - (defender.defense * 2), 1)
    defender.health -= damage
    print(f"{attacker.name} наносит {damage} урона! У {defender.name} осталось {defender.health} HP")
def battle(player, enemy):
    start_battle(player, enemy)
    while player.health > 0 and enemy.health > 0:
        print(f"Ваше текущее здоровье: {player.health} HP")
        print(">>>Меню действий<<<")
        print("1. Атаковать")
        print("2. Защищаться")
        print("3. Проверить врага")
        print("4. Бежать")
        try:
            battle_choice = int(input("Ваш выбор:"))
        except ValueError:
            print("Выберите только из предложенных вариантов")
            continue
        if battle_choice > 4 or battle_choice < 1:
            print("Выберите только из предложенных вариантов")
            continue
        if battle_choice == 1:
            attack_battle(player, enemy)
            attack_battle(enemy, player)
        elif battle_choice == 2:
            defense_battle(player, enemy)
        elif battle_choice == 3:
            enemy.show_stats()
        elif battle_choice == 4:
            print("Вы успешно сбежали!\nВы получили 0 золота и 0 опыта")
            save(player)
            return
    if player.health <= 0:
        print("Вы погибли! Возвращаем вас в главное меню...")
        player.health = player.max_health
        return
    if enemy.health <= 0:
        print(f"Вы победили! Вы получили {enemy.exp_loot} опыта и {enemy.money_loot} золота!")
        player.money += enemy.money_loot
        player.exp += enemy.exp_loot
        player.lvl_up()
        player.health = player.max_health
        save(player)
        return