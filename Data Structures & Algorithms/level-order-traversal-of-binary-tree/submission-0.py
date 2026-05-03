# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = [root]

        res = []
        while len(q) > 0:
            temp = []
            for i in range(len(q)):
                te = q.pop(0)
                temp.append(te.val)
                if te.left:
                    q.append(te.left)
                if te.right:
                    q.append(te.right)

            res.append(temp)
        return res
            
