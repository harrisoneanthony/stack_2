class Vehicle:
    vehicle_list = []
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.seat_belt = True
        Vehicle.vehicle_list.append(self)

    @classmethod
    def vehicle_info(cls):
        for car in cls.vehicle_list:
            print(car.brand)

    def drive(self):
        print("Car is driving")

    def specific_vehicle_info(self):
        print(self.model, self.year)


nissan = Vehicle("Nissan", "GTR", 2022, "black")
kia = Vehicle("Kia", "Stinger", 2018, "silver")

# print(nissan)
# print(nissan.model)
# nissan.vehicle_info()
# kia.vehicle_info()

Vehicle.vehicle_info()

kia.specific_vehicle_info()