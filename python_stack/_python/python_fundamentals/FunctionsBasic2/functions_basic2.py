# 1. Countdown
def countdown(num):
    output = []
    for i in range(num, -1, -1):
        output.append(i)
    return output

print("--- 1. Countdown ---")
print(countdown(5)) 


# 2. Print and Return
def print_and_return(nums_list):
    print(nums_list[0])
    return nums_list[1]

print("\n--- 2. Print and Return ---")
result = print_and_return([1, 2])
print(f"Returned value: {result}") 


# 3. First Plus Length
def first_plus_length(nums_list):
    return nums_list[0] + len(nums_list)

print("\n--- 3. First Plus Length ---")
print(first_plus_length([1, 2, 3, 4, 5])) 


# 4. Values Greater than Second
def values_greater_than_second(orig_list):
    if len(orig_list) < 2:
        return False
    
    new_list = []
    second_val = orig_list[1]
    
    for val in orig_list:
        if val > second_val:
            new_list.append(val)
            
    print(len(new_list))
    return new_list

print("\n--- 4. Values Greater than Second ---")
print(values_greater_than_second([5, 2, 3, 2, 1, 4])) 
print(values_greater_than_second([3])) 

# 5. This Length, That Value
def length_and_value(size, value):
    output = []
    for i in range(size):
        output.append(value)
    return output

print(length_and_value(4, 7)) 
print(length_and_value(6, 2)) 