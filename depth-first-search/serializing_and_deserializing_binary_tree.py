class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(node):
        if not node:
            return ['x']
        arr = []
        arr += [node.val]
        arr += dfs(node.left)
        arr += dfs(node.right)
        return arr

    return ' '.join(dfs(root))

def deserialize(s):
    # AND HERE
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    return build_tree(iter(s.split(' ')))

if __name__ == '__main__':
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    def print_tree(root):
        if not root:
            yield "x"
            return
        yield str(root.val)
        yield from print_tree(root.left)
        yield from print_tree(root.right)
    input = '10 86 x x 100 x x'
    root = build_tree(iter(input.split()))
    new_root = deserialize(serialize(root))
    print(' '.join(print_tree(new_root)))