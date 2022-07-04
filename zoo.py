class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        self.__animals += 1
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}"

    def get_count(self):
        return self.__animals


name = input()
n = int(input())
zoo = Zoo(name)

for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)
species_name = input()
print(zoo.get_info(species_name))
print(f"Total animals: {zoo.get_count()}")
