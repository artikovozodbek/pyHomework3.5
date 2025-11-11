people = {
    "Bill Gates": "Dasturchi",
    "Cristiano Ronaldo": "Futbolchi",
    "Elon Musk": "Tadbirkor",
    "Messi": "Futbolchi"
}

name = input("Ismni kiriting: ")

professions = people.get(name)

if professions:
    print(f"{name} ning kasbi: {professions}")
else:
    print("Bunday ism topilmadi!.")