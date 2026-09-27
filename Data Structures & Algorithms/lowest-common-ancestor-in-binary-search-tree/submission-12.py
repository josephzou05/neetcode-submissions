# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        #keep going down a single path until p and q have a split
        while current:
            #1) both values smaller than curr
            if p.val < current.val and q.val < current.val:
                current = current.left
            #2) both values larger than curr
            elif p.val > current.val and q.val > current.val:
                current = current.right
            #3) else
            else:
                return current
