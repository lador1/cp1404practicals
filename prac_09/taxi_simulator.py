from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """(C)hoose taxi
(D)rive
(Q)uit"""


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("Choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()
    print("Taxis are now:")
    display_taxis(taxis)
    print(f"Total bill is ${total_bill}")


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()
"""NOTES:"""
"""Create class for movies, enter movies in list"""
