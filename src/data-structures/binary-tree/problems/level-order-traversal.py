# https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
    
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                r: TreeNode = queue.popleft()
                current_level.append(r.val)
                if r.left:
                    queue.append(r.left)
                
                if r.right:
                    queue.append(r.right)
            result.append(current_level)

        return result
        