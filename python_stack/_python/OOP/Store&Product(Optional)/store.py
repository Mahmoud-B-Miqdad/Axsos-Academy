from product import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, product_id):
        for i, product in enumerate(self.products):
            if product.id == product_id:
                product.print_info()
                self.products.pop(i)
                return
        print(f"Product with ID {product_id} not found.")

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)

    def print_inventory(self):
        print(f"\n--- Current Inventory in {self.name} ---")
        for product in self.products:
            product.print_info()