class Underscore:
    def map(self, iterable, callback):
        result = []
        for item in iterable:
            result.append(callback(item))
        return result

    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                return item
        return None

    def filter(self, iterable, callback):
        result = []
        for item in iterable:
            if callback(item):
                result.append(item)
        return result

    def reject(self, iterable, callback):
        result = []
        for item in iterable:
            if not callback(item):
                result.append(item)
        return result

_ = Underscore()

print("Map (x*2):", _.map([1, 2, 3], lambda x: x * 2))

print("Find (>4):", _.find([1, 2, 3, 4, 5, 6], lambda x: x > 4)) 

print("Filter (even):", _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)) 

print("Reject (even):", _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)) 