# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        tres = []
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(tres) == depth:
                tres.append([])

            tres[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        
        for l in tres:
            res.append(l[-1])


        return res