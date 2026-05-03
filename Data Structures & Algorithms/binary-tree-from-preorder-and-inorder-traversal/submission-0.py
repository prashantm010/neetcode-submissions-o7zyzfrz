# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_mp = {inorder[i] : i for i in range(len(inorder))}
        self.index = 0

        def helper(left, right):
            if left > right:
                return

            val = preorder[self.index]
            self.index += 1
            root = TreeNode(val)

            mid = self.inorder_mp[val]

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder)-1)
