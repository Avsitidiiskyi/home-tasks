import sys
# from tqdm import tqdm, trange
from time import sleep


class Car:
    def __init__(self, model, body: str = ''):
        self.model = model
        self.body = body
        self.doors = 4
        self.engine = 2.0
        self.speed_limit = 280

    def car_description(self):
        desc = f"Model is: {self.model}, body & chassis type : {self.body}, engine {self.engine}, " \
               f"maximum speed = {self.speed_limit} contains {self.doors} doors"
        return print(desc)

    def speed_determination(self):
        speed = int(input("Enter speed:  "))
        if speed > 280:
            print("Speed limit has been exceeded")
            sys.exit()
        else:
            pass
        return speed

    def drive(self):
        print(f'car drives with speed: {self.speed_determination()}')

    def armour(self):

        print('Armour 100%')

        # for defence in trange(100, desc='ARMOUR', leave=True, disable=False, ncols=100):
        #     sleep(0.01)
        #
        # return defence

    def engine_modify(self):
        self.engine += 3.0

    def doors_modify(self):
        self.doors -= 2


#
car1 = Car("Volkswagen Passat", 'Universal')

James_Bond_car = Car('Aston Martin', "Sport")

car1.drive()
car1.car_description()
print('-----James Bond car------')
James_Bond_car.engine_modify()
James_Bond_car.doors_modify()
James_Bond_car.drive()
James_Bond_car.car_description()
James_Bond_car.armour()


class Plane:
    def __init__(self, plane_class, plane_name, engine_type, wingspan, fuselage_diameter):
        self.plane_class = plane_class
        self.plane_name = plane_name
        self.engine_type = engine_type
        self.wingspan = wingspan
        self.fuselage_diameter = fuselage_diameter
        self.max_high = 1000
        self.range_of_flight = 2300
        self.speed_limit = 500

    def plane_description(self):
        desc = f"Plane class is: {self.plane_class}, Engine type: {self.engine_type}, " \
               f"wingspan = {self.wingspan} meters, fuselage_diameter =  {self.fuselage_diameter} metres"
        return print(desc)

    def high_modify(self):
        self.max_high += 9000

    def range_modify(self):
        self.range_of_flight += 8500

    def speed_modify(self):
        self.speed_limit += 350

    def flight_description(self):
        print(
            f'{self.plane_description()}, {self.plane_name} flights on {self.max_high}, '
            f'its maximum range of flight is {self.range_of_flight}, limited by the speed {self.speed_limit}')

    def estimation(self):
        est = self.range_of_flight / self.speed_limit

        return print(f"Flight takes {round(est)} minutes to reach the destination")


plane1 = Plane("AH-2", 'Kukuruznik', "Turboprop", 6, 2)
plane_x = Plane("Boeing-777", 'Passenger', "Gas Turbine Engine", 28, 12)
print('---Flight information---')
plane1.flight_description()
plane1.estimation()


plane_x.high_modify()
plane_x.range_modify()
plane_x.speed_modify()
print('--------------------------')
plane_x.flight_description()
plane_x.estimation()


class Ship:
    destiny_1 = 'was sunk on  May 27  1941, during the battle'
    destiny_2 = 'sunk after collision with an iceberg in the Atlantic ocean in 1912'

    def __init__(self, ship_class, ship_name, displacement, length, high, width, engine_power):
        self.ship_class = ship_class
        self.ship_name = ship_name
        self.displacement = displacement
        self.length = length
        self.high = high
        self.width = width
        self.engine_power = engine_power
        self.crew = 2200
        self.sailing_range = 9280

    def ship_description(self):
        desc = f"{self.ship_name}, Ship class: {self.ship_class}, Water displacement: {self.displacement}," \
               f" length = {self.length} meters. Height =  {self.high} metres, " \
               f"{self.width} metres width. Engine = {self.engine_power} HP, " \
               f"crew = {self.crew}, Max range = {self.sailing_range}"
        return print(desc)

    def crew_update(self):
        self.crew -= 1301

    def sailing_range_update(self):
        self.sailing_range += 3000

    def destiny(self, n):
        print(f'{self.ship_name}, {self.ship_description()}, {n}')


ship_1 = Ship("Lincor", "Bismark", 50900, 241, 15, 36, 150170)
ship_1.destiny(Ship.destiny_1)

ship_2 = Ship('Passenger', "Titanic", 52310, 269, 18, 28, 55000)
print('\n')
ship_2.crew_update()
ship_2.sailing_range_update()
ship_2.destiny(Ship.destiny_2)


class Hybrid(Car, Ship):

    def __init__(self, weapon, *args, **kwargs):
        super(Car).__init__(*args, **kwargs)
        self.weapon = weapon

    @staticmethod
    def max_ground_speed(n):
        max = car1.engine * n
        return max

    @staticmethod
    def max_water_speed(n):
        max = car1.engine * n
        return max

    def description(self, people):
        desc = f"Model is {car1.model}, body is: {car1.body}, weapon is {self.weapon}, " \
               f"crew = {ship_1.crew - people}, engine = {hybrid1.max_ground_speed(100)}, " \
               f"water_engine = {hybrid1.max_water_speed(20)}, water displacement = {ship_1.displacement - 50800}"

        return print(desc)


hybrid1 = Hybrid('X-Gun')

print("\n")
print('Hybrid description')
hybrid1.description(2180)

