from typing import List

def knapsack_weight_only(weights: List[int]) -> List[int]:
    def generate_sums(weights1, sums, sum, n):
        if n == 0:
            sums.add(sum)
            return
        generate_sums(weights1, sums, sum, n - 1)
        generate_sums(weights1, sums, sum + weights1[n - 1], n - 1)
    sums = set()
    n = len(weights)
    generate_sums(weights, sums, 0, n)
    return list(sums)
    

if __name__ == '__main__':
    input = '1 3 3 5'
    weights = [int(x) for x in input.split()]
    res = knapsack_weight_only(weights)
    res.sort()
    for i in range(len(res)):
      print(res[i], end='')
      if i != len(res) - 1:
        print(' ', end='')
    print()