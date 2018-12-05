class EuropeanSocket:
    voltage = 220
    live = 1
    neutral = -1
    earth = 0

class AmericanSocket:
    voltage = 110
    live = 1
    neutral = -1
    earth = None

class AmericanKettle:
    def __init__(self, socket):
        self.socket = socket

    def boil(self):
        if self.socket.voltage > 110:
            print('Kettle on fire!!')
        elif self.socket.voltage == 110 and not self.socket.earth:
            print('Cofee time!!')
        else:
            print('No power!!')

class Adapter:
    def __init__(self, socket):
        self.socket = socket #type: AmericanSocket
    
    @property
    def voltage(self):
        if self.socket.voltage == 220:
            return 110
        else:
            return 220
    @property
    def live(self):
        return self.socket.live
    
    @property
    def neutral(self):
        return self.socket.neutral

    @property
    def earth(self):
        return self.socket.earth
