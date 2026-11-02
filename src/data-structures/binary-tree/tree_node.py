from collections import deque
from dataclasses import dataclass

@dataclass(eq=False)
class TreeNode():
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None    

def create_binary_tree(values: list[int | None]) -> TreeNode:
    root = TreeNode(val=values[0])
    queue = deque()
    
    queue.append(root)
    i = 1
    while queue and i < len(values):
        parent: TreeNode = queue.popleft()
        if values[i] is not None:
            parent.left = TreeNode(val=values[i])
            queue.append(parent.left)
        i += 1
        
        if i < len(values):
            if values[i] is not None:
                parent.right = TreeNode(val=values[i])
                queue.append(parent.right)
        i += 1

    return root