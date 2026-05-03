# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INT_MIN = float("-inf")
        INT_MAX = float("inf")

        return self.isValidBSTUtil(root, INT_MIN, INT_MAX)

    def isValidBSTUtil(self, root, min_, max_):
        if root is None:
            return True

        if min_ >= root.val or max_ <= root.val:
            return False

        return self.isValidBSTUtil(root.left, min_, root.val) and self.isValidBSTUtil(root.right, root.val, max_)
        