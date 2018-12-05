# A Factory is an interface to produce an object
# But it deffers the instantiation to runtime

class Shape:
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        print('drawing a square..')

class Circle(Shape):
    def draw(self):
        print("Drawing a circle...")


class ShapeFactory:
    
    @staticmethod
    def get_shape(type):
        if type == 'square':
            return Square()
        elif type == 'circle':
            return Circle()
        else:
            return None

if __name__ == "__main__":
    ShapeFactory.get_shape('circle').draw()
