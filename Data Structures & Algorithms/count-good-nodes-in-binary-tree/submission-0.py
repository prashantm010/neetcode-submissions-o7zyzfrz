# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return -1

        q = [(root, root.val)]
        c = 0
        while q:
            n = len(q)
            for i in range(n):
                t, max = q.pop(0)
                if t.val >= max:
                    c += 1
                    max = t.val
                if t.left:
                    q.append((t.left, max))
                if t.right:
                    q.append((t.right, max))

        return c