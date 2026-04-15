from animal import Animal

class Lion(Animal):
    def __init__(self, name, age, pride_size=5):
        super().__init__(name, age) 
        self.pride_size = pride_size 

    def feed(self):
        self.health_level += 20 
        print(f"The lion {self.name} ate like a beast! Health increased by 20.")
        return self