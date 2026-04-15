from zoo import Zoo
from lion import Lion
from tiger import Tiger
from monkey import Monkey

my_zoo = Zoo("The Grand Zoo")

simba = Lion("simba", 5)
rajah = Tiger("rajah", 4, 45)
abu = Monkey("abu", 3)

my_zoo.add_animal(simba)
my_zoo.add_animal(rajah)
my_zoo.add_animal(abu)

print("--- Starting the feeding process ---")
simba.feed()
rajah.feed()
abu.feed()

my_zoo.print_all_info()