from random import randint
class Warrior:
    health = 60
    def __init__(self, name):
        self.name = name
    def make_kick(self, enemy):
        enemy.health -= 20
        print(self.name, "бьет", enemy.name)
        print(f'{enemy.name} - {enemy.health} здовровья')

class Battle:
    result = 'Сражения не было'
    def battle(self, u1, u2):
        while u1.health > 0 and u2.health > 0:
            n = randint(1, 2)
            if n == 1:
                u1.make_kick(u2)
            else:
                u2.make_kick(u1)
        if u1.health > u2.health:
            self.result = u1.name + ' Победил'
        elif second.health > first.health:
            self.result = u2.name + ' Победил'
    def who_win(self):
        print(self.result)


first = Warrior('Германец')
second = Warrior('Римлянин')
b = Battle()
b.battle(first, second)
b.who_win()


