
class Animal:
    def __init__(self, name):
        self._name = name
        self._eat = None

    def get_name(self):
        return self._name

    def make_sound(self):
        pass

    def eat(self):
        print(f"eat {self._eat}")


class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self._color = color
        self._eat = "wheat"

    def make_sound(self):
        print(f"{self._name} makes a sound 'Tweet'")


class Mammal(Animal):
    def __init__(self, name, average_life_span):
        super().__init__(name)
        self._average_life_span = average_life_span
        self._eat = "grass"

    def make_sound(self):
        print(f"{self._name} makes a sound 'Meow'")


class Reptile(Animal):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size
        self._eat = "slime"

    def make_sound(self):
        print(f"{self._name} makes a sound 'Hiss'")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
        animal.eat()


class Staff:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name)

    def feed_animal(self, animal):
        print(f"{self.get_name()} feed animal {animal.get_name()}")


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name)

    def heal_animal(self, animal):
        print(f"{self.get_name()} heal animal {animal.get_name()}")


class Zoo:
    def __init__(self, name):
        self._name = name
        self._animals = []
        self._staff = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)

    def add_staff(self, employee):
        self._staff.append(employee)

    def remove_staff(self, employee):
        self._staff.remove(employee)

    def show_animals(self):
        for animal in self._animals:
            print(animal.get_name())

    def list_staff(self):
        for employee in self._staff:
            print(employee.get_name())


animal_sound([Bird("Pigeon", "white"), Mammal("Koala", 5),
              Reptile("Crocodile", "large")])

zoo = Zoo("My Zoo")
zoo.add_animal(Bird("Toucan", "colorful"))
zoo.add_animal(Mammal("Zebra", 12))
zoo.add_animal(Reptile("Python", "medium"))

veterinarian = Veterinarian("Dr. Smith")
zoo.add_staff(veterinarian)
zookeeper1 = ZooKeeper("Jack Evil")
zoo.add_staff(zookeeper1)
zookeeper2 = ZooKeeper("Lucy Good")

zoo.show_animals()
zoo.list_staff()

zoo._staff[1].feed_animal(zoo._animals[1])  # Смотритель кормит животное
zoo._staff[0].heal_animal(zoo._animals[0])  # Ветеринар лечит животное