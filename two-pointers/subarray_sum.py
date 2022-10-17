from typing import List

def big_o_n_2(arr: List[int], target: int) -> List[int]:
    a = 0
    while a <= len(arr):
        sum = 0
        for b in range(a, len(arr)):
            sum += arr[b]
            if sum == target:
                return [a, b + 1]
        a += 1

def big_o_n(arr: List[int], target: int) -> List[int]:
    prefix_sums = [0]
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            return [prefix_sums.index(complement), i + 1]
        prefix_sums.append(cur_sum)

if __name__ == '__main__':
    input = '1 3 -3 8 5 7'
    target = 5
    arr = [int(x) for x in input.split()]
    res = big_o_n(arr, target)
    print(' '.join(map(str, res)))
