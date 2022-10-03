from typing import List

def big_o_n(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    mid, count = 0, 0
    for i in range(0, len(arr)):
        count += 1
        if arr[i] < arr[mid]:
            mid = i
    print(f'minimum integer is {arr[mid]}, index is {mid}, loop count is {count}')
    return mid

def big_o_log_n(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary, count = 0, 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[len(arr) - 1]:
            boundary = mid
            right = mid - 1
        elif arr[mid] > arr[len(arr) - 1]:
            left = mid + 1
        count += 1
    print(f'minimum integer is {arr[boundary]}, index is {boundary}, loop count is {count}')
    return boundary

if __name__ == '__main__':
    input = '30 40 50 10 20'
    arr = [int(x) for x in input.split()]
    big_o_n(arr)
    big_o_log_n(arr)
