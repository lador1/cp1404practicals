from prac_09.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi(name='Lamborghini', fuel=100, fanciness=2)
taxi.drive(18)
print(taxi)
print(taxi.get_fare())