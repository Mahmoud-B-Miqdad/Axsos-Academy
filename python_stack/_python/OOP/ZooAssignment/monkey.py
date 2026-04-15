from animal import Animal

class Monkey(Animal):
    def __init__(self, name, age, intelligence=80):
        super().__init__(name, age)
        self.intelligence = intelligence

    def feed(self):
        self.health_level += 15
        self.happiness_level += 15
        print(f"The monkey {self.name} enjoyed the bananas! Health and happiness increased by 15.")
        return self