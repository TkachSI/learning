# 1. Реализуйте базовый класс Car.
# У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Реализовать метод для user-friendly вывода информации об автомобиле.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print("Скорость: ", speed)

    @classmethod
    def go(cls):
        # поехали
        return "Поехали"

    @classmethod
    def stop(cls):
        # остановились
        return "Остановились"

    @staticmethod
    def turn(direction):
        # новернули
        return f"Повернули: {direction}"

    def show_speed(self):
        return f"Текущая скорость: {self.speed}"


class TownCar(Car):
    def show_speed(self):
        # новернули
        if self.speed > 60:
            res = self.speed - 40
            return f"Привышение скорости на {res}!!"
        return f"Вы движетесь с разрешенной скоростью {self.speed}"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        # новернули
        if self.speed > 40:
            res = self.speed - 40
            return f"Привышение скорости на {res}!!"
        return f"Вы движетесь с разрешенной скоростью {self.speed}"


class PoliceCar(Car):
    pass


# speed, color, name, is_police
car1 = Car(111, "pink", "Ford", False)
car2 = Car(59, "red", "Mercedes", False)
car3 = Car(140, "white", "Ferrari", True)
car4 = Car(40, "yellow", "Porsche", False)
car5 = Car(60, "dark", "BMW", True)

car6 = TownCar(90, "dark", "BMW", True)
print(car6.turn("left"))
print(car6.show_speed())
