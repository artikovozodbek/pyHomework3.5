car_count = {
    "Chevrolet": 120,
    "Toyota": 95,
    "BMW": 60,
    "Kia": 75
}

max_car = max(car_count, key=car_count.get)
min_car = min(car_count, key=car_count.get)

print(max_car)
print(min_car)