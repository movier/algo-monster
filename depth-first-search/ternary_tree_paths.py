from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(node, path, res):
        if len(node.children) == 0:
            res.append('->'.join(path) + '->' + str(node.val))
            return
        for c in node.children:
            path.append(str(node.val))
            dfs(c, path, res)
            path.pop()
    res = []
    dfs(root, [], res)
    return res

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == '__main__':
    input = '1 3 2 1 5 0 3 0 4 0'
    root = build_tree(iter(input.split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)