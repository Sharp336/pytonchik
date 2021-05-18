from random import randrange
from random import randint
import math
class Gaym():
        
    def start(self):
        answer = input('Привет! Мы шиз.. фигуры и у нас есть 2 вопроса\n\nОтветите на них ?\n\nДа - нажмите Enter\nНет - введите что угодно.\n')
        if answer == '':
            r = randint(0,3)
            if r == 0:
                self.rectangle()
            if r == 1:
                self.triangle()
            if r == 2:
                self.circle()
            if r == 3:
                self.quadrat()
            
        
    def rectangle(self):
        self.__side1 = randint(1,100)
        self.__side2 = randint(1,100)
        self.__area = self.__side1 * self.__side2
        self.__perimeter = self.__side1 * 2 + self.__side2 * 2
        self.__text = f'прямоугольник со сторонами {self.__side1} и {self.__side2}'
        self.go()
        
    def triangle(self):
        self.__perimeter = randrange(12,1000,12)
        self.hp = self.__perimeter / 2
        self.__side1 = randrange(self.__perimeter / 3,self.hp - 2,2)
        self.__side2 = randrange(self.__perimeter / 3,self.hp - 2,2)
        self.__side3 = self.__perimeter - self.__side1 - self.__side2
        self.__area = round(math.sqrt(self.hp * (self.hp - self.__side1) * (self.hp - self.__side2) * (self.hp - self.__side3)))
        self.__text = f'треугольник со сторонами {self.__side1} и {self.__side2} и {self.__side3}'
        self.go()
    
    def circle(self):
        self.__radius = randint(1, 100)
        self.__area = round(math.pi * self.__radius ** 2)
        self.__perimeter = round(self.__radius * 2 * math.pi)
        self.__text = f'круг с радиусом {self.__radius}'
        self.go()
        
    def quadrat(self):
        self.__side1 = randint(1,100)
        self.__area = self.__side1 ** 2
        self.__perimeter = self.__side1 * 4
        self.__text = f'квадрат со стороной {self.__side1}'
        self.go()
        
    def go(self):
        print(f'Я - {self.__text}')
        q1 = input('Укажите площадь для данной фигуры:\nP.S. округлить до целых\n')
        if int(q1) == self.__area:
            q2 = input('Правильно!\nУкажите периметр для данной фигуры:\nP.S. округлить до целых\n')
            if int(q2) == self.__perimeter: print('Правильно!')
            else: print(f'Ошибка! Правильный ответ: {self.__perimeter}')
        else: print(f'Ошибка! Правильный ответ: {self.__area}')
        q3 = input('Играем ещё ?\n\nДа - нажмите Enter\nНет - введите что угодно.\n')
        if q3 == '': self.start()
        print('Спасибо за игру :)')
        
        
g = Gaym()
g.start()