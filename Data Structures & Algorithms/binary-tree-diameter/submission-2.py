class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0  # best diameter in edges

        def height(node):
            if not node:
                return 0  # height in edges from node down (or 0 in nodes-count style)
            
            left = height(node.left)
            right = height(node.right)

            # path through this node uses left + right edges
            self.best = max(self.best, left + right)

            # return height to parent
            return 1 + max(left, right)

        height(root)
        return self.best