import math, random

class Rectangle:
    def __init__(self):
        self.side1 = random.randint(1,1000)
        self.side2 = random.randint(1,1000)
        self.area = self.side1 * self.side2
        self.perimeter = self.side1 * 2 + self.side2 * 2
        self.text = f'прямоугольник со сторонами {self.side1} и {self.side2}'
        
class Triangle:
    
    def __init__(self):
        self.perimeter = random.randrange(24,1000,12)
        self.hp = self.perimeter / 2
        self.side1 = random.randrange(self.perimeter / 3,self.hp - 2,2)
        self.side2 = random.randrange(self.perimeter / 3,self.hp - 2,2)
        self.side3 = self.perimeter - self.side1 - self.side2
        self.area = round(math.sqrt(self.hp * (self.hp - self.side1) * (self.hp - self.side2) * (self.hp - self.side3)))
        self.text = f'треугольник со сторонами {self.side1} и {self.side2} и {self.side3}'

class Circle:
    
    def __init__(self):
        self.radius = random.randint(1, 666)
        self.area = round(math.pi * self.radius ** 2)
        self.perimeter = round(self.radius * 2 * math.pi)
        self.text = f'круг с радиусом {self.radius}'
        
class Quadrat:
    
    def __init__(self):
        self.side1 = random.randint(1,616)
        self.area = self.side1 ** 2
        self.perimeter = self.side1 * 4
        self.text = f'квадрат со стороной {self.side1}'

while True:
    
    figure = None
    answer = input('Привет! Мы шиз.. фигуры и у нас есть 2 вопроса\n\nОтветите на них ?\n\nДа - нажмите Enter\nНет - введите что угодно.\n')
    if answer == '':
        r = random.randint(0,3)
        if r == 0:
            figure = Rectangle()
        elif r == 1:
            figure = Triangle()
        elif r == 2:
            figure = Circle()
        elif r == 3:
            figure = Quadrat()
    else:
        print('Вы умерли.\nТак сложно ответить на пару вопросов ?')
        break
        
    print(f'Я - {figure.text}')
    q1 = input('Укажите площадь для данной фигуры:\nP.S. округлить до целых\n')
    if q1.isnumeric() and int(q1) == figure.area:
        q2 = input('Правильно!\nУкажите периметр для данной фигуры:\nP.S. округлить до целых\n')
        if q2.isnumeric() and int(q2) == figure.perimeter: print('Правильно!')
        else: print(f'Ошибка! Правильный ответ: {figure.perimeter}')
    else: print(f'Ошибка! Правильный ответ: {figure.area}')
    q3 = input('Играем ещё ?\n\nДа - нажмите Enter\nНет - введите что угодно.\n')
    if q3 != '':
        print('Спасибо за игру :)')
        break