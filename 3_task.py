#Создайте Автомобиль, который может ехать. Ехать он может когда у него заполнен бак(переменная)
#Пользователь может заправить автомобиль, вызвав соответствующий метод,Поездка в зависимости от расстояния тратит топливо.
#1(л)к10(км)

class Car:

    fuel = 0

    def refueling(self, fuel_new):
        fuel_quantity = int(input("Enter the amount of fuel - "))
        fuel_new += fuel_quantity
        self.fuel = fuel_new
        print("In your fuel tank",fuel_new, "liter")

    def drive(self):
        max_distance = self.fuel / 10
        print("Maximum distance", max_distance, "kilometers")
        distance = float(input("Enter the distance "))
        if distance <= max_distance:
            way = max_distance - distance
            print("You drove", distance, "kilometers. You can still drive", way, "kilometers")
        else:
            print("Not enough fuel for the trip")


car = Car()
car.refueling(0)
car.drive()



