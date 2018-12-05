class Singleton:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if Singleton.__instance == None:
            Singleton.__instance = object.__new__(cls)
        else:
            Singleton.__instance.__init__(*args, **kwargs)
        return Singleton.__instance

class Another(Singleton):
    def __init__(self, a, b):
        self.a = a
        self.b = b


if __name__ == "__main__":
    s1 = Another(2,3)
    print(s1)
    s2 = Another(5,7)
    print(s2)
    print('===============')
    print(s1 == s2)
    print(s1 is s2)