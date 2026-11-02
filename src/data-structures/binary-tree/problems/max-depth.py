# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        max_left = self.maxDepth(root.left)
        max_right = self.maxDepth(root.right)

        return 1 + max(max_left, max_right)
        