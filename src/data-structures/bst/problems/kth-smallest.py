# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        
        curr_node = root
        nodes = []

        while k:
            while curr_node:
                nodes.append(curr_node)
                curr_node = curr_node.left
            
            curr_node = nodes.pop()
            k -= 1
            if not k:
                break
            
            curr_node = curr_node.right
            
                
        return curr_node.val
                