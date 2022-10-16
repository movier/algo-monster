def decode_ways(digits: str) -> int:
    memo = {}
    def dfs(start_index, memo):
        if start_index in memo:
            return memo[start_index]
        if start_index == len(digits):
            return 1

        ways = 0
        if digits[start_index] == '0':
            return ways
        ways += dfs(start_index + 1, memo)
        if 10 <= int(digits[start_index: start_index + 2]) <= 26:
            ways += dfs(start_index + 2, memo)

        memo[start_index] = ways
        return ways

    return dfs(0, memo)

if __name__ == '__main__':
    input = '12'
    digits = input
    res = decode_ways(digits)
    print(res)