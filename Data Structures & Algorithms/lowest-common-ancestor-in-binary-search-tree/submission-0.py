# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        a, b = p.val, q.val
        cur = root

        if a > cur.val and b > cur.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if a < cur.val and b < cur.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return cur