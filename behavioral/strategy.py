class AbstractOddFinder:
    def __init__(self, limit):
        self.limit = limit

    def calculate(self):
        pass
    
    def Out(self):
        print(self.__class__.__name__)
        print(self.calculate())

class HardCodedOddFinder(AbstractOddFinder):
    def calculate(self):
        odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
        result = []
        for o in odds:
            if o <= self.limit:
                result.append(o)
        return result

class StandardOddFinder(AbstractOddFinder):
    def calculate(self):
        result = [o for o in range(self.limit) if o%2 == 1]
        return result

class Client:
    def __init__(self, limit):
        if limit <= 29:
            self.finder = HardCodedOddFinder(limit)
        else:
            self.finder = StandardOddFinder(limit)
    def calculate(self):
        self.finder.Out()

