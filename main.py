from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Класс, представляющий бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        print(self.weapon.attack())

# Класс, представляющий монстра
class Monster:
    def __init__(self, name):
        self.name = name

    def is_defeated(self):
        print(f"{self.name} побежден!")

# Демонстрация боя
def main():
    # Создаем бойца с мечом
    fighter = Fighter(Sword())
    monster = Monster("Монстр")

    print("Боец выбирает меч.")
    fighter.attack()
    monster.is_defeated()

    # Меняем оружие бойца на лук
    print("\nБоец выбирает лук.")
    fighter.change_weapon(Bow())
    fighter.attack()
    monster.is_defeated()

if __name__ == "__main__":
    main()
