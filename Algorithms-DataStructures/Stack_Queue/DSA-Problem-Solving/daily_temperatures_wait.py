class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0

def daily_temperatures(temps):
    n = len(temps)
    result = [0] * n
    stack = Stack()  

    for i in range(n):
        while not stack.is_empty() and temps[i] > temps[stack.peek()]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        
        stack.push(i)
        
    return result

example_temps = [22, 18, 28, 32, 25, 20, 23]
print(f"Temperatures: {example_temps}")
print(f"Days until warmer: {daily_temperatures(example_temps)}")