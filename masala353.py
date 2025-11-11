cars = {
    "Tesla": 250,
    "BMW": 240,
    "Mercedes": 260,
    "Audi": 230
}

sorted_cars = sorted(cars.items(), key=lambda x: x[1], reverse=True)

for name, speed in sorted_cars:
    print(name, speed)