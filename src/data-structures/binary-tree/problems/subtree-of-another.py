# https://leetcode.com/problems/subtree-of-another-tree/
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
    
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root is None and subRoot is None:
            return True
        elif subRoot is None:
            return True
        elif root is None:
            return False
    
        queue = deque([root])
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
               return True
        while queue:
            r: TreeNode = queue.popleft()
            if r.left:
                if r.left.val == subRoot.val:
                    if self.isSameTree(r.left, subRoot):
                        return True
                queue.append(r.left)
            
            if r.right:
                if r.right.val == subRoot.val:
                    if self.isSameTree(r.right, subRoot):
                        return True
                queue.append(r.right)
            
        return False
        