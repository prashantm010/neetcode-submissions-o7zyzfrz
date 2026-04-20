# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None or p.val != q.val:
                return False

            return isSame(p.left, q.left) and isSame(p.right, q.right)

        def dfs(node):
            if node is None:
                return False
            
            if isSame(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)
        