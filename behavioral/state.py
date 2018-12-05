class ComputerState:
    allowed = []
    name = 'generic state'
    
    def switch(self, state):
        if state.name in self.allowed:
            print('Current state ' + str(self) + '==> Switched to ' + state.name)
            self.__class__ = state
        else:
            print('Current state ' + str(self) + '==> Switching to ' + state.name + ' is not possible')
    
    def __str__(self):
        return self.name

class On(ComputerState):
    allowed = ['off', 'suspend', 'hibernate']
    name = 'on'

class Off(ComputerState):
    allowed = ['on']
    name = 'off'

class Suspend(ComputerState):
    allowed = ['on']
    name = 'suspend'

class Hibernate(ComputerState):
    allowed = ['on']
    name = 'hibernate'

class Computer:
    def __init__(self):
        self.state = Off()

    def change_state(self, new_state):
        self.state.switch(new_state)

