class Engine:
    def start(self, starting_speed):
        if starting_speed < 3000:
            return False
        else: 
            return True


class Battery:
    def __init__(self):
        self.power = 0

    def charge(self, charging_power):
        if charging_power < 1000:
            return False
        else:
            self.power = charging_power
            return True

class Starter:
    def __init__(self):
        self.speed = 0

    def start(self, battery_power):
        if battery_power >=1000:
            self.speed = battery_power * 0.75
            return True
        else:
            return False

class Car:
    def __init__(self):
        self.battery = Battery()
        self.starter = Starter()
        self.engine = Engine()

    def charge_battery(self, charging_power):
        self.battery.charge(charging_power)

    def turn_key(self):
        starter_started = self.starter.start(self.battery.power)
        if starter_started:
            print('Starter started..')
            engine_started = self.engine.start(self.starter.speed)
            if engine_started:
                print('Engine Started..')
            else:
                print('Engine failed to start, no enough starter speed..')
        else:
            print('Starter failed to start, no enough battery power..')


if __name__ == "__main__":
    import pdb; pdb.set_trace()