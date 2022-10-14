from typing import List

def letter_combination(n: int) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(start_index, path):
        if start_index == n:
            res.append(''.join(path))
            return
        for letter in ['a', 'b']:
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()
    
    res = []
    dfs(0, [])
    return res

if __name__ == '__main__':
    input = '6'
    n = int(input)
    res = letter_combination(n)
    for line in sorted(res):
        print(line)
