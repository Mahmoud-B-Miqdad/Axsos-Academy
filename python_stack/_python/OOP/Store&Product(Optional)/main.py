from product import Product
from store import Store

my_store = Store("Tech World")

p1 = Product("Laptop", 1000, "Electronics", 1)
p2 = Product("Mouse", 50, "Electronics", 2)
p3 = Product("Coffee Mug", 10, "Kitchen", 3)

my_store.add_product(p1)
my_store.add_product(p2)
my_store.add_product(p3)

print("--- Testing Inflation ---")
my_store.inflation(0.1) 
p1.print_info()

print("\n--- Testing Clearance ---")
my_store.set_clearance("Electronics", 0.2)
p1.print_info()

my_store.print_inventory()
print("\n--- Testing Selling Product ---")
my_store.sell_product(2) 
my_store.print_inventory()