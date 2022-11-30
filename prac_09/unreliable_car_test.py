from prac_09.unreliable_car import UnreliableCar

bad_car = UnreliableCar(name="Maserati", fuel=90, reliability=50)
good_car = UnreliableCar(name="Toyota", fuel=90, reliability=100)

for i in range(1, 10):
    print(f"Attempting to drive {i}km:")
    print(f"{good_car.name:} drove: {good_car.drive(i):}km")
    print(f"{bad_car.name:} drove: {bad_car.drive(i):}km")

    # print the final states of the cars
    print(good_car)
    print(bad_car)


