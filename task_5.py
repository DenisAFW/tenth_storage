# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.


class Animals:
    def __init__(self, name):
        self.name = name

    def animal_name(self):
        return f'Имя: {self.name}'


class Fish(Animals):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def get_info(self):
        return f'Глубина обитания: {self.depth} М '


class Birds(Animals):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def get_info(self):
        return f'Размах крыльев: {self.wingspan} см '


class Reptiles(Animals):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def get_info(self):
        return f'Длина тела:  {self.length} М '


class AnimalFactory:
    def __init__(self):
        self.animal_classes = {
            'Fish': Fish,
            'Birds': Birds,
            'Reptiles': Reptiles
        }

    def create_animal(self, animal_type, *args):
        if animal_type not in self.animal_classes:
            raise ValueError("Invalid animal type")

        animal_class = self.animal_classes[animal_type]
        return animal_class(*args)


if __name__ == '__main__':
    factory = AnimalFactory()
    fish = factory.create_animal('Fish', 'Som', 5)
    bird = factory.create_animal('Birds', 'Parrot', 10)
    reptile = factory.create_animal('Reptiles', 'Anaconda', 3)
    print(fish.animal_name())
    print(fish.get_info())
    print(bird.animal_name())
    print(bird.get_info())
    print(reptile.animal_name())
    print(reptile.get_info())
