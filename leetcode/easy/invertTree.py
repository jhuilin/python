def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def invertTree(self, root):
    if root == None:
        return root
    stack = [root]
    while len(stack) != 0:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root