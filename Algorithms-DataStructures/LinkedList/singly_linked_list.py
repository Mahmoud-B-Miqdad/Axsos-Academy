class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    # Add a new node to the front of the list
    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self

    # Add a new node to the end of the list
    def add_to_back(self, val):
        if self.head is None:
            self.add_to_front(val)
            return self
        
        # Traverse to the last node
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        
        # Point the last node to the new node
        runner.next = SLNode(val)
        return self

    # NINJA BONUS: remove_from_front
    def remove_from_front(self):
        if self.head:
            self.head = self.head.next
        return self

    # NINJA BONUS: remove_from_back
    def remove_from_back(self):
        if not self.head: return self
        if not self.head.next:
            self.head = None
            return self
        
        runner = self.head
        while runner.next.next:
            runner = runner.next
        runner.next = None
        return self

    # NINJA BONUS: remove_val
    def remove_val(self, val):
        if not self.head: return self
        if self.head.value == val:
            self.remove_from_front()
            return self
        
        runner = self.head
        while runner.next:
            if runner.next.value == val:
                runner.next = runner.next.next
                return self
            runner = runner.next
        return self

    # SENSEI BONUS: insert_at
    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self
        
        new_node = SLNode(val)
        runner = self.head
        count = 0
        while runner and count < n - 1:
            runner = runner.next
            count += 1
        
        if runner:
            new_node.next = runner.next
            runner.next = new_node
        return self

    # Print all values in the list
    def print_values(self):
        runner = self.head
        while runner:
            print(runner.value, end=" -> ")
            runner = runner.next
        print("None")
        return self

my_list = SList()

print("--- Adding nodes ---")
my_list.add_to_front(10).add_to_front(5).add_to_back(20).add_to_back(30)
my_list.print_values() 

print("\n--- Testing removals ---")
my_list.remove_from_front() 
my_list.remove_from_back()  
my_list.print_values()      

my_list.add_to_back(40)     
my_list.remove_val(20)      
my_list.print_values()      

print("\n--- Testing insert_at ---")
my_list.insert_at(25, 1)   
my_list.print_values()      

print("\n--- Testing edge cases ---")
empty_list = SList()
empty_list.remove_from_front() 
empty_list.insert_at(100, 0)   
empty_list.print_values()     