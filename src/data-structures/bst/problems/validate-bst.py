# https://leetcode.com/problems/validate-binary-search-tree
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        queue = deque([(root, float("-inf"), float("inf"))])
        while queue:
            r = queue.popleft()
            if r[0].left:
                if r[0].left.val >= r[0].val or r[0].left.val <= r[1]:
                    return False
                queue.append([r[0].left, r[1], r[0].val])
            
            if r[0].right:
                if r[0].right.val <= r[0].val or r[0].right.val >= r[2]:
                    return False
                queue.append([r[0].right, r[0].val, r[2]])
            
        return True