from typing import List

def permutations(letters: str) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(letters, path):
        if len(letters) == 0:
            res.append(''.join(path))
            return
        for l in letters:
            path.append(l)
            dfs(list(filter(lambda x: x != l, letters)), path)
            path.pop()
    res = []
    dfs(letters, [])
    return res

if __name__ == '__main__':
    input = 'abcd'
    letters = input
    res = permutations(letters)
    for line in sorted(res):
        print(line)
