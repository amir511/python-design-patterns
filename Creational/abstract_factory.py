# Shape Interfaces

class Shape2DInterface:
    def draw(self):
        pass

class Shape3DInterfac:
    def build(self):
        pass

# Shape Concrete classes

class Circle(Shape2DInterface):
    def draw(self):
        print('Drawing a circle...')

class Square(Shape2DInterface):
    def draw(self):
        print('Drawing a square...')

class Sphere(Shape3DInterfac):
    def build(self):
        print('Building a Sphere..')

class Cube(Shape3DInterfac):
    def build(self):
        print('Building a cube...')


# Abstract Shape Factory 
class ShapeAbstractFactory:
    @staticmethod
    def get_shape(sides):
        pass
# Concrete 2D shape factory
class Shape2DFactory(ShapeAbstractFactory):
    @staticmethod
    def get_shape(sides):
        if sides == 1:
            return Circle()
        elif sides == 4:
            return Square()
        else:
            raise Exception('Wrong number of sides, should be either 1 or 4')

# Concrete 3D shape factory
class Shape3DFactory(ShapeAbstractFactory):
    @staticmethod
    def get_shape(sides):
        if sides == 1:
            return Sphere()
        elif sides == 12:
            return Cube()
        else:
            raise Exception('Wrong number of sides, should be either 1 or 12')



if __name__ == "__main__":
    import pdb; pdb.set_trace()