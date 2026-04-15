def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

data = [12, 11, 13, 5, 6]
print("The array befor sort", data)

sorted_data = insertion_sort(data)
print("The array after sort", sorted_data)