class Animal:
    def __init__(self, name):
        self._name = name
        self._eat = None

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


animal_sound([Bird("Pigeon", "white"), Mammal("Koala", 5),
              Reptile("Crocodile", "large")])
