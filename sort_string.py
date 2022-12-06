def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

print(quicksort([10, 5, 2, 7, 1, 3]))
print(quicksort(["apple", "orange", "banana", "grape"]))
print(quicksort(["John", "Michael", "Emily", "Jessica"]))