
class Animal:
    def __init__(self, name):
        self._name = name
        self._eat = None
        self._kind = None

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

    def properties_to_str(self):
        return f"Bird,{self.get_name()},{self._color}"


class Mammal(Animal):
    def __init__(self, name, average_life_span):
        super().__init__(name)
        self._average_life_span = average_life_span
        self._eat = "grass"

    def make_sound(self):
        print(f"{self._name} makes a sound 'Meow'")

    def properties_to_str(self):
        return f"Mammal,{self.get_name()},{self._average_life_span}"

class Reptile(Animal):
    def __init__(self, name, size, is_poisonous=False):
        super().__init__(name)
        self._size = size
        self._eat = "slime"
        self.is_poisonous = is_poisonous

    def make_sound(self):
        print(f"{self._name} makes a sound 'Hiss'")

    def properties_to_str(self):
        return f"Reptile,{self.get_name()},{self._size},{self.is_poisonous}"


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
        animal.eat()


class Staff:
    def __init__(self, name):
        self._name = name
        self._profession = None

    def get_name(self):
        return self._name


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name)
        self._profession = "ZooKeeper"

    def feed_animal(self, animal):
        print(f"{self.get_name()} feed animal {animal.get_name()}")


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name)
        self._profession = "Veterinarian"

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

    def add_staff(self, person):
        self._staff.append(person)

    def remove_staff(self, person):
        self._staff.remove(person)

    def show_animals(self):
        if len(self._animals) > 0:
            for animal in self._animals:
                print(animal.get_name())
        else:
            print("No animals")

    def list_staff(self):
        if len(self._staff) > 0:
            for person in self._staff:
                print(f"{person.get_name()} - {person._profession}")
        else:
            print("No staff")

    def save_state(self):
        with open("state.txt", 'w') as file:
            for person in self._staff:
                file.write(f"staff,{person.get_name()},{person._profession}\n")

            for animal in self._animals:
                file.write(f"animal,{animal.properties_to_str()}\n")

        print("Zoo state saved to file.")

    def restore_state(self):
        with open("state.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith("staff"):
                    name, profession = line.split(",")[1:]
                    if profession == "ZooKeeper":
                        self.add_staff(ZooKeeper(name))
                    elif profession == "Veterinarian":
                        self.add_staff(Veterinarian(name))
                    else:
                        print(f"Unrecognized profession: {profession}")

                elif line.startswith("animal"):
                    if line.split(",")[1] == "Bird":
                        self.add_animal(Bird(line.split(",")[2], line.split(",")[3]))
                    elif line.split(",")[1] == "Mammal":
                        self.add_animal(Mammal(line.split(",")[2], line.split(",")[3]))
                    elif line.split(",")[1] == "Reptile":
                        self.add_animal(Reptile(line.split(",")[2], line.split(",")[3], bool(line.split(",")[4])))  # bool(line.split(",")[4])
                    else:
                        print(f"Unrecognized animal: {line.split(',')}")


print('= check polymorphism')
animal_sound([Bird("Pigeon", "white"), Mammal("Koala", 5),
              Reptile("Crocodile", "large")])

print('= check class Zoo')
zoo = Zoo("My Zoo")
zoo.add_animal(Bird("Toucan", "colorful"))
zoo.add_animal(Mammal("Zebra", 12))
zoo.add_animal(Reptile("Python", "medium"))
zoo.add_animal(Reptile("Cobra", "long", True))

veterinarian = Veterinarian("Dr. Smith")
print(veterinarian.__class__)
print(veterinarian.__class__.__name__)
print(str(veterinarian.__dict__))

zoo.add_staff(veterinarian)
zookeeper1 = ZooKeeper("Jack Evil")
zoo.add_staff(zookeeper1)
zookeeper2 = ZooKeeper("Lucy Good")
zoo.add_staff(zookeeper2)

zoo.show_animals()
zoo.list_staff()

# не совсем корректно обращаться напрямую к защищенным полям, но для примера
zoo._staff[1].feed_animal(zoo._animals[1])  # Смотритель кормит животное
zoo._staff[0].heal_animal(zoo._animals[0])  # Ветеринар лечит животное

print('= check save and restore state')
zoo.save_state()

print('= check clear animals and staff')
zoo._animals = []
zoo._staff = []

zoo.show_animals()
zoo.list_staff()

zoo.restore_state()

print('= check restore animals and staff')
zoo.show_animals()
zoo.list_staff()

