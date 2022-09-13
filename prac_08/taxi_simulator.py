from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
taxis = [Taxi("Pirus", 100), SilverServiceTaxi('Limo', 100, 2), SilverServiceTaxi('Hummer', 100, 4)]
print("Let's drive!")
print(MENU)


def main():
    """main function for taxi simulator"""
    total_bill = 0
    current_taxi = None
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == 'c':
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = get_valid_choice()
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == 'd':
            if current_taxi:
                current_taxi.start_fare()
                current_taxi.drive(float(input("Drive how far? ")))
                trip_cost = current_taxi.get_fare()
                total_bill += trip_cost
                print(f"Your {current_taxi} trip cost you ${trip_cost:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

    while menu_choice not in ['c', 'q', 'd']:
        print("Invalid option")
        print(MENU)
        menu_choice = input(">>> ").lower()
    return menu_choice


def display_taxis(vehicles):
    """Display vehicles"""
    for i, vehicle in enumerate(vehicles):
        print("{} - {}".format(i, vehicle))


def get_valid_choice():
    """Validate input"""
    value_input = False
    while not value_input:
        try:
            menu_choice = int(input("Choose Taxi: "))
            value_input = True
            return menu_choice
        except ValueError:
            print("Incorrect input type.")


main()
