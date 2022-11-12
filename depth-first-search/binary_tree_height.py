class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_height(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(node):
        if not node:
            return 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)

        return max(left_height, right_height) + 1

    return dfs(root)

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    input = '5 4 3 x x 8 x x 6 x x'
    root = build_tree(iter(input.split()), int)
    res = binary_tree_height(root)
    print(res)