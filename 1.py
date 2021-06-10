from random import randint, random
from typing import List


class Fighter:
    def __init__(self, name: str):
        self.name = name
        self.height = randint(160, 200)
        self.weight = randint(60, 100)
        self.power = randint(75, 100)
        self.crit = 5 if ((self.height - 160) + (self.weight - 60) - 30) <= 5 else ((self.height - 160) + (self.weight - 60) - 30)
        self.dodge = 5 if -((self.height - 200) + (self.weight - 100)) -20 <= 5 else -((self.height - 200) + (self.weight - 100)) -20
        self.health = 100


class Contest:
    winner: Fighter
    @classmethod
    def new(cls, first: Fighter, second: Fighter) -> None:
        cls.fighters = [first, second]
        cls.first, cls.second = cls.fighters.pop(round(random())), cls.fighters.pop()
        print(
            f'{first.name}: Рост: {first.height}, Вес:{first.weight}, Сила:{first.power}')
        print(
            f'{second.name}: Рост: {second.height}, Вес:{second.weight}, Сила:{second.power}')
        print(
            '----------------------------------------------------')
        print(
            f'По жребию начинает {cls.first.name}')
        while first.health > 0 and second.health > 0:
            if randint(0, 100) <= second.dodge:
                print(f'{second.name} успешно отразил удар')
            else:
                if randint(0, 100) <= first.crit:
                    second.health -= round(first.power * 0.2)
                    print(f'{first.name} нанёс критический урон: {round(first.power * 0.2)}')
                    print(f'{second.name}: Отхватил: {round(first.power * 0.2)}, Здоровья: {second.health}')
                else:
                    second.health -= round(first.power * 0.1)
                    print(f'{second.name}: Отхватил: {round(first.power * 0.1)}, Здоровья: {second.health}')
            if second.health <= 0: 
                print(f'{second.name} мертв!\nПобедил: {first.name}')
                break
            if randint(0, 100) <= first.dodge:
                print(f'{first.name} успешно отразил удар')
            else:
                if randint(0, 100) <= first.crit:
                    first.health -= round(second.power * 0.2)
                    print(f'{second.name} нанёс критический урон: {round(second.power * 0.2)}')
                    print(f'{first.name}: Отхватил: {round(second.power * 0.1)}, Здоровья: {first.health}')
                else:
                    first.health -= round(second.power * 0.1)
                    print(f'{first.name}: Отхватил: {round(second.power * 0.1)}, Здоровья: {first.health}')
            if first.health <= 0: 
                print(f'{first.name} мертв!\nПобедил: {second.name}')
                break


a = Fighter('Ваня')
b = Fighter('Саня')

f = Contest()
f.new(a,b)