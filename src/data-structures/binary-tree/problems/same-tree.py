# https://leetcode.com/problems/same-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque 
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
            
    
        if p.val != q.val:
            return False
        queue1 = deque([p])
        queue2 = deque([q])
        
        while queue1 and queue2:
            r1: TreeNode = queue1.popleft()
            r2: TreeNode = queue2.popleft()
            if r1.left and r2.left:
                if r1.left.val != r2.left.val:
                    return False
                queue1.append(r1.left)
                queue2.append(r2.left)
            elif r1.left or r2.left:
                return False

            if r1.right and r2.right:
                if r1.right.val != r2.right.val:
                    return False
                queue1.append(r1.right)
                queue2.append(r2.right)
            elif r1.right or r2.right:
                return False
        
        return True