class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        lines = []
        def dfs(node, prefix="", is_left=True):
            
            if node is None:
                return
            
            dfs(node.right, prefix + ("│   " if is_left else "    "), False)
            lines.append(prefix + ("└── " if is_left else "┌── ") + str(node.val))
            dfs(node.left, prefix + ("    " if is_left else "│   "), True)

        dfs(self)
        return "\n".join(lines)

def print_tree(root: Node | None):
    def dfs(node, prefix="", is_left=True):
        if node is None:
            return
        dfs(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        dfs(node.left, prefix + ("    " if is_left else "│   "), True)
    dfs(root)

def serialize(node: Node) -> str:
    s = []
    
    def str_repr(node: Node | None):
        if node is None:
            s.append("NONE")
            return
        
        s.append(node.val)
        str_repr(node.left)
        str_repr(node.right)
    
    str_repr(node)
    return ';'.join(s)

def deserialize(s: str) -> Node | None:
    s_iter = iter(s.split(';'))

    def build():
        nd = next(s_iter)
        if nd == "NONE":
            return None
        node = Node(nd)
        node.left = build()
        node.right = build()
        return node

    if not s:
        return None
    return build()
    

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    node_s = serialize(node)
    node_ds = deserialize(node_s)
    print(node_s)
    print(node_ds)
    assert deserialize(serialize(node)).left.left.val == 'left.left'