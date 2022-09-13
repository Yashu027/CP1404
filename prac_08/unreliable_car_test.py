from prac_08.unreliable_car import UnreliableCar


def main():
    """Compare two cars"""
    new_car = UnreliableCar('New Ferrari', 100, 90)  # more reliable
    old_car = UnreliableCar('Old Ferrari', 100, 10)  # less reliable
    new_car.drive(50)
    old_car.drive(50)
    print(new_car)
    print(old_car)


main()
