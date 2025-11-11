import os
os.system("cls")

cars = {
    "Malibu": 35000,
    "Spark": 12000,
    "Cobalt": 18000,
    "Tracker": 28000
}

car_max = max(cars, key=cars.get)
car_min = min(cars, key=cars.get)

print("Eng qimmat mashina:",car_max)
print("Eng arzon mashina:",car_min)

average_price = sum(cars.values()) / len(cars)

print("O'rtacha narx:",average_price)