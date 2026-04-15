class Zoo:
    def __init__(self, name):
        self.animals = []
        self.name = name

    def add_animal(self, animal):
        self.animals.append(animal)
        return self

    def print_all_info(self):
        print("-" * 20, f"Garden: {self.name}", "-" * 20)
        for animal in self.animals:
            animal.display_info()