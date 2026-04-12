# 1. Biggie Size
def biggie_size(nums_list):
    for i in range(len(nums_list)):
        if nums_list[i] > 0:
            nums_list[i] = "big"
    return nums_list

print("--- 1. Biggie Size ---")
print(biggie_size([-1, 3, 5, -5])) 

# 2. Count Positives
def count_positives(nums_list):
    count = 0
    for val in nums_list:
        if val > 0:
            count += 1
    nums_list[len(nums_list)-1] = count
    return nums_list

print("\n--- 2. Count Positives ---")
print(count_positives([-1, 1, 1, 1])) 
print(count_positives([1, 6, -4, -2, -7, -2])) 

# 3. Sum Total
def sum_total(nums_list):
    total = 0
    for val in nums_list:
        total += val
    return total

print("\n--- 3. Sum Total ---")
print(sum_total([1, 2, 3, 4])) 
print(sum_total([6, 3, -2]))   

# 4. Average
def average(nums_list):
    if len(nums_list) == 0:
        return 0
    return sum_total(nums_list) / len(nums_list)

print("\n--- 4. Average ---")
print(average([1, 2, 3, 4])) 


# 5. Length
def length(nums_list):
    return len(nums_list)

print("\n--- 5. Length ---")
print(length([37, 2, 1, -9])) 
print(length([]))          

# 6. Minimum
def minimum(nums_list):
    if len(nums_list) == 0:
        return False
    
    min_val = nums_list[0]
    for val in nums_list:
        if val < min_val:
            min_val = val
    return min_val

print("\n--- 6. Minimum ---")
print(minimum([37, 2, 1, -9])) 
print(minimum([]))       


# 7. Maximum
def maximum(nums_list):
    if len(nums_list) == 0:
        return False
    
    max_val = nums_list[0]
    for val in nums_list:
        if val > max_val:
            max_val = val
    return max_val

print("\n--- 7. Maximum ---")
print(maximum([37, 2, 1, -9])) 
print(maximum([]))            


# 8. Ultimate Analysis
def ultimate_analysis(nums_list):
    analysis = {
        'sumTotal': sum(nums_list),
        'average': sum(nums_list) / len(nums_list) if len(nums_list) > 0 else 0,
        'minimum': minimum(nums_list),
        'maximum': maximum(nums_list),
        'length': len(nums_list)
    }
    return analysis

print("\n--- 8. Ultimate Analysis ---")
print(ultimate_analysis([37, 2, 1, -9])) 


# 9. Reverse List
def reverse_list(nums_list):
    for i in range(0, len(nums_list) // 2):
        temp = nums_list[i]
        nums_list[i] = nums_list[len(nums_list) - 1 - i]
        nums_list[len(nums_list) - 1 - i] = temp
    return nums_list

print("\n--- 9. Reverse List ---")
print(reverse_list([37, 2, 1, -9])) 