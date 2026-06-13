class Character:
    def __init__(self, name, level, money, health, max_health, attack, defense, character_class):
        self.name = name
        self.level = level
        self.money = money
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.defense = defense
        self.character_class = character_class
        self.exp = 0
        self.exp_needed = 100
        self.inventory = []
    def lvl_up(self):
        while self.exp >= self.exp_needed and self.level < 100:
            self.level += 1
            self.attack += 5
            self.defense += 3
            self.exp -= self.exp_needed
            self.exp_needed += 50
            print(f"Вы успешно подняли уровень! Ваш уровень: {self.level}")
    def show_stats(self):
        print("Ваши характеристики:")
        print(f"Имя: {self.name}\nУровень: {self.level}\nДеньги: {self.money}")
        print(f"Здоровье: {self.health}\nУрон: {self.attack}\nЗащита: {self.defense}\nКласс: {self.character_class}")
        print(f"Опыт: {self.exp}\nНеобходимый опыт для поднятия уровня: {self.exp_needed}")
    def show_stats_registration(self):
        print(f"Стартовые деньги: {self.money}, Здоровье: {self.health}")
        print(f"Стартовый урон: {self.attack}, Стартовая защита: {self.defense}")
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, level=1, money=0, health=80, max_health=80, attack=35, defense=5, character_class="Маг")

class Tank(Character):
    def __init__(self, name):
        super().__init__(name, level=1, money=0, health=150, max_health=150, attack=10, defense=25, character_class="Танк")

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, level=1, money=100, health=100, max_health=100, attack=20, defense=15, character_class="Разбойник")
class Enemy:
    def __init__(self, name, attack, health, defense, exp_loot, money_loot):
        self.name = name
        self.attack = attack
        self.health = health
        self.defense = defense
        self.exp_loot = exp_loot
        self.money_loot = money_loot
    def show_stats(self):
        print("Характеристика врага:")
        print(f"Название врага: {self.name}, Урон: {self.attack}")
        print(f"Здоровье: {self.health}, Защита: {self.defense}")
class WeakGoblin(Enemy):
    def __init__(self):
        super().__init__(name="Слабый гоблин", attack=25, defense=5, health=50, exp_loot=25, money_loot=50)
class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Гоблин",attack=50, defense=10, health=80, exp_loot=50, money_loot=100)