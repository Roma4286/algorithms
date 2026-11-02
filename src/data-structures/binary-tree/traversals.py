from collections import deque
from tree_node import TreeNode, create_binary_tree

r = create_binary_tree([1, 2, 3, 4, None, None, 5, None, 6, None, 7, None, None, 8])

def preorder(root: TreeNode) -> list[int]:
    if not root:
        return []
        
    res = []
    res.append(root.val)
    if root.left:
        r1 = preorder(root.left)
        res.extend(r1)
    if root.right:
            r2 = preorder(root.right)
            res.extend(r2)

    return res

print(preorder(r))

def inorder(root: TreeNode) -> list[int]:
    if not root:
        return []
        
    res = []
    if root.left:
        r1 = inorder(root.left)
        res.extend(r1)
    res.append(root.val)

    if root.right:
            r2 = inorder(root.right)
            res.extend(r2)

    return res

print(inorder(r))

def postorder(root: TreeNode) -> list[int]:
    if not root:
            return []
    
    res = []
    if root.left:
        r1 = postorder(root.left)
        res.extend(r1)

    if root.right:
            r2 = postorder(root.right)
            res.extend(r2)

    res.append(root.val)

    return res

print(postorder(r))

def level_order(root: TreeNode) -> list[int]:
    if not root:
        return []
    
    queue = deque([root])
    result = [root.val]
    while queue:
        r: TreeNode = queue.popleft()
        if r.left:
            result.append(r.left.val)
            queue.append(r.left)
        
        if r.right:
            result.append(r.right.val)
            queue.append(r.right)
        
    return result

print(level_order(r))