# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        k = 0
        return self.dfswithK(root, k)

    def dfswithK(self, root, k):
        if not root:
            return k
        k+=1
        while True:
            num1 = self.dfswithK(root.left, k)
            num2 = self.dfswithK(root.right, k)
            return max(num1, num2)
