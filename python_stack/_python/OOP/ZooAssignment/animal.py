class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health_level = 50  
        self.happiness_level = 50

    def display_info(self):
        print(f"Animal: {self.name} | Health: {self.health_level} | Happiness: {self.happiness_level}")
        return self

    def feed(self):
        self.health_level += 10
        self.happiness_level += 10
        print(f"{self.name} has been fed! Health and happiness have increased.")
        return self