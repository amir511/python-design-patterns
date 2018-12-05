class Car:
    def __init__(self):
        self.wheels = None
        self.engine = None
        self.body = None
        self.model = None

    def set_body(self, body):
        self.body = body

    def set_wheels(self, wheels):
        self.wheels = wheels

    def set_engine(self, engine):
        self.engine = engine
    
    def set_model(self, model):
        self.model = model

    def get_specs(self):
        specs =  '''Car with model type:{}
                    It has body shape: {}
                    It has {} wheels
                    with size {} each
                    HP of engine: {}
        '''.format(
            self.model.name, self.body.shape, len(self.wheels), self.wheels[0].size, self.engine.hp
        )
        return specs

class Wheel:
    size = None
class Engine:
    hp = None
class Model:
    name = None
class Body:
    shape = None

class CarBuilderInterface:
    def get_model(self):pass
    def get_body(self):pass
    def get_wheels(self):pass
    def get_engine(self):pass

class BMWbuilder(CarBuilderInterface):
    def get_model(self):
        model = Model()
        model.name = 'BMW'
        return model
    def get_engine(self):
        engine = Engine()
        engine.hp = 200
        return engine

    def get_body(self):
        body = Body()
        body.shape = 'passenger'
        return body

    def get_wheels(self):
        wheel = Wheel()
        wheel.size = 20
        wheels = [wheel for i in range(4)]
        return wheels

class JeepBuilder(CarBuilderInterface):
    def get_model(self):
        model = Model()
        model.name = 'Jeep'
        return model
    def get_engine(self):
        engine = Engine()
        engine.hp = 400
        return engine

    def get_body(self):
        body = Body()
        body.shape = 'SUV'
        return body

    def get_wheels(self):
        wheel = Wheel()
        wheel.size = 22
        wheels = [wheel for i in range(6)]
        return wheels

class Director:
    builder = None

    def set_builder(self, builder):
        self.builder = builder #type: BMWbuilder
    
    def get_car(self):
        car = Car()
        car.set_body(self.builder.get_body())
        car.set_engine(self.builder.get_engine())
        car.set_model(self.builder.get_model())
        car.set_wheels(self.builder.get_wheels())
        return car

if __name__ == "__main__":
    import pdb; pdb.set_trace()


