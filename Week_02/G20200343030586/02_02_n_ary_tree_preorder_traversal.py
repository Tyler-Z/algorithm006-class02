# 589. N叉树的前序遍历
# 根左右

# 递归
"""
class Solution(object):
    def preorder(self, root):

        # terminator
        if not root:
            return []
        ans=[]

        # current lvl
        def preTreversal(node):
            if not node:
                return
            ans.append(node.val)        #先将当前节点的值写入数组ans[]中
            for cur in node.children:   #前序遍历，对于每一个孩子，依此递归
                preTreversal(cur)
        preTreversal(root)
        return ans
"""


# 迭代
class Solution(object):
    def preorder(self, root):

        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])

        return output