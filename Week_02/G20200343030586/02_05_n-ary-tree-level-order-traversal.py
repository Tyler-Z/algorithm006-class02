# 429. N叉树的层序遍历

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        q = deque([root])
        res = []
        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                for c in cur.children:
                    q.append(c)
                level.append(cur.val)
            res.append(level)
        return res
