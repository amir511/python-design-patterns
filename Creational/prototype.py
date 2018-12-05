from copy import deepcopy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point at ({},{})'.format(self.x, self.y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def clone(self, new_x, new_y):
        new_point = deepcopy(self)
        new_point.move_to(new_x, new_y)
        return new_point

# Different approach
class Prototype:
    def clone(self):
        return deepcopy(self)

class ConcretePrototype(Prototype):

    def __init__(self, a):
        self.a = a

    def do_something(self):
        print('doing something')

if __name__ == "__main__":
    import pdb; pdb.set_trace()

