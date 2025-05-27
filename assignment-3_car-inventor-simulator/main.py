# This program creates a Car object, a Truck object,
# and an SUV object with random unique values each time.

import vehicles
import random


def generate_random_car():
    makes = ['BMW', 'Audi', 'Honda', 'Ford']
    year = random.randint(1995, 2020)
    mileage = random.randint(20000, 150000)
    price = round(random.uniform(5000, 20000), 2)
    doors = random.choice([2, 4])
    return vehicles.Car(random.choice(makes), year, mileage, price, doors)


def generate_random_truck():
    makes = ['Toyota', 'Chevrolet', 'Dodge', 'Nissan']
    year = random.randint(1995, 2020)
    mileage = random.randint(20000, 150000)
    price = round(random.uniform(5000, 20000), 2)
    drive_type = random.choice(['2WD', '4WD'])
    return vehicles.Truck(random.choice(makes), year, mileage, price, drive_type)


def generate_random_suv():
    makes = ['Volvo', 'Jeep', 'Hyundai', 'Subaru']
    year = random.randint(1995, 2020)
    mileage = random.randint(20000, 150000)
    price = round(random.uniform(7000, 25000), 2)
    pass_cap = random.randint(4, 8)
    return vehicles.SUV(random.choice(makes), year, mileage, price, pass_cap)


def main():
    car = generate_random_car()
    truck = generate_random_truck()
    suv = generate_random_suv()

    print('USED CAR INVENTORY')
    print('=====================')

    print('The following car is in inventory:')
    print('Make:', car.get_make())
    print('Model:', car.get_model())
    print('Mileage:', car.get_mileage())
    print('Price:', car.get_price())
    print('Number of doors:', car.get_doors())
    print()

    print('The following truck is in inventory:')
    print('Make:', truck.get_make())
    print('Model:', truck.get_model())
    print('Mileage:', truck.get_mileage())
    print('Price:', truck.get_price())
    print('Drive type:', truck.get_drive_type())
    print()

    print('The following SUV is in inventory:')
    print('Make:', suv.get_make())
    print('Model:', suv.get_model())
    print('Mileage:', suv.get_mileage())
    print('Price:', suv.get_price())
    print('Passenger Capacity:', suv.get_pass_cap())


# Call the main function
main()
