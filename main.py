class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _ins(node, val):
            if not node: return Node(val)
            if val < node.val: node.left  = _ins(node.left,  val)
            elif val > node.val: node.right = _ins(node.right, val)
            return node
        self.root = _ins(self.root, val)

    def search(self, val):
        def _srch(node, val):
            if not node: return False
            if val == node.val: return True
            return _srch(node.left, val) if val < node.val else _srch(node.right, val)
        return _srch(self.root, val)

    def inorder(self):
        result = []
        def _in(node):
            if node:
                _in(node.left)
                result.append(node.val)
                _in(node.right)
        _in(self.root)
        return result

    def height(self):
        def _h(node):
            if not node: return 0
            return 1 + max(_h(node.left), _h(node.right))
        return _h(self.root)

if __name__ == "__main__":
    bst = BST()
    for v in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(v)
    print("Inorder:", bst.inorder())   # [1,3,4,5,6,7,8]
    print("Search 4:", bst.search(4))  # True
    print("Height:", bst.height())     # 3
