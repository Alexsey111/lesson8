import random
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self, attacker, target):
        pass

class Sword(Weapon):
    def attack(self, attacker, target):
        target.health -= attacker.sword_damage
        print(f'{attacker.name} наносит удар мечом.')
        print(f'Здоровье {target.name}: {target.health}')

class Bow(Weapon):
    def attack(self, attacker, target):
        target.health -= attacker.bow_damage
        print(f'{attacker.name} стреляет из лука.')
        print(f'Здоровье {target.name}: {target.health}')

class Fighter:
    def __init__(self, name, health, sword_damage, bow_damage):
        self.name = name
        self.health = health
        self.sword_damage = sword_damage
        self.bow_damage = bow_damage
        self.weapon = None

    def set_weapon(self, weapon):
        self.weapon = weapon

    def attack(self, target):
        self.weapon.attack(self, target)

class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        target.health -= self.damage
        print(f'{self.name} наносит удар. У {target.name} осталось {target.health} здоровья.')

def fight(monster, fighter):
    print(f"Бой начинается! {fighter.name} против {monster.name}!")
    first_attacker = random.choice([fighter, monster])
    while monster.health > 0 and fighter.health > 0:
        if first_attacker == fighter:
            fighter.attack(monster)
            if monster.health > 0:
                monster.attack(fighter)
        else:
            monster.attack(fighter)
            if fighter.health > 0:
                fighter.attack(monster)
    if monster.health <= 0:
        print(f'{monster.name} побежден!')
    elif fighter.health <= 0:
        print(f'{fighter.name} мертв.')


monster = Monster('Дракон', 300, 50)
fighter = Fighter('Пересвет', 150, 150, 100)
fighter.set_weapon(Sword() if random.choice([True, False]) else Bow())

fight(monster, fighter)
