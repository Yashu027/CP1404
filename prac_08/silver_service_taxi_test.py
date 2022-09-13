from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    service_taxi = SilverServiceTaxi("Service Taxi", 100, 2)
    print(service_taxi)
    print(f"{service_taxi.drive(18)}km drive by {service_taxi}")
    print(f"The total fare for the trip is ${service_taxi.get_fare():.2f}")


main()
