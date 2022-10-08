from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) - 1
    mid = 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] < arr[mid - 1]:
            right = mid - 1
        elif arr[mid] < arr[mid + 1]:
            left = mid + 1
    return mid

if __name__ == '__main__':
    input = '30 40 50 10 20'
    arr = [int(x) for x in input.split()]
    res = peak_of_mountain_array(arr)
    print(res)