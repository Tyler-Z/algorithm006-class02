# 590. N叉树的后序遍历
# 后续遍历：左、右、根

"""
def postorder(root)

    if root:
        postorder(root.left)
        postorder(root.right)
        traverse_path.append(root.val)
"""


def postorder(root):

    if root is None:
        return []

    stack, output = [root, ], []

    while stack:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
        for c in root.children:
            stack.append(c)

    return output[::-1]