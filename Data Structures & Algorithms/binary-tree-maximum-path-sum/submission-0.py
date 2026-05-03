# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_ = float("-inf")

        def dfs(root):
            if root is None:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            curr = root.val + left + right

            self.max_ = max(self.max_, curr)

            return root.val + max(left, right)

        dfs(root)
        return self.max_

