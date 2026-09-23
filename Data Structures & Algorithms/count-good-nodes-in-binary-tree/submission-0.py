# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        def dfs(node, x):
            nonlocal good
            if not node:
                return
            
            if node.val >= x:
                good += 1
            
            x = max(node.val, x)
            
            dfs(node.right, x)
            dfs(node.left, x)
        
        dfs(root, root.val)
        
        return good