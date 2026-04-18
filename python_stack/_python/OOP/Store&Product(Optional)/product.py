class Product:
    def __init__(self, name, price, category, product_id):
        self.name = name
        self.price = price
        self.category = category
        self.id = product_id 

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self.price

    def print_info(self):
        print(f"Product: {self.name}, Category: {self.category}, Price: ${self.price:.2f}, ID: {self.id}")