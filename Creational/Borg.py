class Borg:
    _shared_state = {}
    def __init__(self, a, b):
        self.__dict__ = self._shared_state
        self.a = a
        self.b = b

if __name__ == "__main__":
    b = Borg(2,3)
    b2 = Borg(1,10)