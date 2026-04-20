# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def height(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1

            return 1 + max(height(root.left), height(root.right))

        lh = height(root.left)
        rh = height(root.right)

        return abs(lh-rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


        