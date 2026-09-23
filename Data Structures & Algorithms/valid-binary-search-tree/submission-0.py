# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lowerBound, upperBound):
            if not node:
                return True

            if not (lowerBound < node.val < upperBound):
                return False

            leftValid = dfs(node.left, lowerBound, node.val)
            rightValid = dfs(node.right, node.val, upperBound)

            return leftValid and rightValid

        return dfs(root, float("-inf"), float("inf"))