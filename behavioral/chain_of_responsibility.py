class Car:

    def __init__(self, oil, water, fuel):
        self.oil = oil
        self.water = water
        self.fuel = fuel

    def is_fine(self):
        if self.oil >= 100 and self.water >= 100 and self.fuel >=100:
            return True
        return False

class BaseHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, car):
        if not car.is_fine() and self.successor != None:
            self.successor.handle(car)
        elif car.is_fine():
            print('Car is good to go!!')
        else:
            print('Car is not ready but we cannot handle it in the mean time!!!')

class OilHandler(BaseHandler):
    def handle(self, car):
        if car.oil <= 100:
            car.oil = 100
            print('Added Oil!')
        super().handle(car)

class WaterHandler(BaseHandler):
    def handle(self, car):
        if car.water <= 100:
            car.water = 100
            print('Added Water')
        super().handle(car)

class FuelHandler(BaseHandler):
    def handle(self, car):
        if car.fuel <= 100:
            car.fuel = 100
            print('Added Fuel')
        super().handle(car)

