class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty!"
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None  

    def is_empty(self):
        return len(self.queue) == 0

def first_non_repeating(stream):
    char_count = {} 
    queue = Queue() 
    result = []

    for char in stream:
        char_count[char] = char_count.get(char, 0) + 1
        
        queue.enqueue(char)
        
        while not queue.is_empty() and char_count[queue.peek()] > 1:
            queue.dequeue()
            
        if not queue.is_empty():
            result.append(queue.peek())
        else:
            result.append('#')
            
    return result

stream = "aabcbd"
output = first_non_repeating(stream)

print(f"Stream: {list(stream)}")
print(f"First non-repeating: {output}")