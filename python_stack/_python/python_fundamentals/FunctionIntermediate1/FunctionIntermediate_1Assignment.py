import random

def randInt(min=0, max=100):
    if min > max:
        min, max = max, min
    
    if max < 0:
        return "Max cannot be less than 0"

    num = (random.random() * (max - min)) + min
    
    return round(num)

print(f"Random 0 to 100: {randInt()}")           
print(f"Random 0 to 50:  {randInt(max=50)}")
print(f"Random 50 to 100: {randInt(min=50)}")     
print(f"Random 50 to 500: {randInt(min=50, max=500)}") 