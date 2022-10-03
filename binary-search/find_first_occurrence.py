from typing import List

def good_code_bad_performance(arr: List[int], target: int) -> int:
    count, answer = 0, -1
    left, right = 0, len(arr) - 1
    while left <= right:
        count += 1
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            answer = mid
            right = mid - 1
    print(f'with good_code_bad_performance, answer is {answer}, loop count is {count}')

def bad_code_good_performance(arr: List[int], target: int) -> int:
    count, answer = 0, -1
    left, right = 0, len(arr) - 1
    while left <= right:
        count += 1
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            if mid == 0 or arr[mid-1] < target:
                answer = mid
                break
            else:
                right = mid - 1
    print(f'with bad_code_good_performance, answer is {answer}, loop count is {count}')
        

if __name__ == '__main__':
    input = '1 3 3 3 3 6 10 10 10 100'
    arr = [int(i) for i in input.split(' ')]
    target = 3
    res1 = good_code_bad_performance(arr, target)
    res2 = bad_code_good_performance(arr, target)
