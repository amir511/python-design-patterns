class Window:
    def build(self):
        print('Window hole...')

class AbstractWindowDecorator:
    def __init__(self, window):
        self.window = window

    def build(self):
        pass

class WindowGlassDecorator(AbstractWindowDecorator):
    def build(self):
        self.window.build()
        print('Window glass added..')

class WindowBorderDecorator(AbstractWindowDecorator):
    def build(self):
        self.window.build()
        print('Window border added ..')

class WindowLockDecorator(AbstractWindowDecorator):
    def build(self):
        self.window.build()
        print('Added Window lock')



