#Есть Алфавит, характеристиками которого являются:
#- Язык
#- Список букв

#Для Алфавита можно:
#- Напечатать все буквы алфавита
#- Посчитать количество букв

class Alphabet:

    def __init__(self, language, letters):
        self.language = language
        self.letters = list(letters)

    def show (self):
        print(self.letters)

    def __len__(self):
        return len(self.letters)




fs = ["a", "b", "c", "d"]
example_1 = Alphabet("English", fs)
example_1.show()
print(example_1.__len__())

