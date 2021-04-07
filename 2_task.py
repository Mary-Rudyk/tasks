#Создать рабочего. У который может ходить на работу.
#Рабочий должен иметь возраст и имя.
#Так же принимать решение идти на работу или нет, в зависимости от того,
#какой ему передали номер дня


class Person:

    name = "Sergei"
    age = 25

    def working(self):
        pass

    def choice(self):
        day = int (input("Write number day (1-7): "))
        if 1 <= day <= 5:
            print("need to work")
        elif day == 6 or day == 7:
            print("no need to work")


workman = Person()
workman.working()
workman.choice()
