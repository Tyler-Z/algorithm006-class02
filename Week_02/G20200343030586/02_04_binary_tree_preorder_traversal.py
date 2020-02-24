# 144. 二叉树的前序遍历

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def helper(root):
            if not root:return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res

