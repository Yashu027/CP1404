import random
from prac_08.car import Car


class UnreliableCar(Car):

    def __init__(self, car_type, fuel, reliability):
        super().__init__(car_type, fuel)
        self.reliability = reliability

    def drive(self, distance):  # Drive the car for given distance, if the car has enough fuel or drive the car until
        # fuel runs out.
        if random.uniform(1, 100) >= self.reliability:
            return distance == 0
        distance_driven = super().drive(distance)
        return distance_driven
