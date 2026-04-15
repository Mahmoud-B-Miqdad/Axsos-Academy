from animal import Animal

class Tiger(Animal):
    def __init__(self, name, age, stripe_count=30):
        super().__init__(name, age)
        self.stripe_count = stripe_count 

    def feed(self):
        self.health_level += 10
        self.happiness_level += 20 
        print(f"The tiger {self.name} jumped for joy with the food! Happiness increased by 20.")
        return self