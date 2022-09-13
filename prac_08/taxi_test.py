from prac_08.taxi import Taxi


def main():

    taxi = Taxi('Prius 1', 100)
    taxi.drive(40)
    print(taxi)
    print(f"After driving the taxi for 40km the Current fare is ${taxi.get_fare():.2f}")
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print(f"After driving the taxi for 100km the Current fare is ${taxi.get_fare():.2f}")


main()
