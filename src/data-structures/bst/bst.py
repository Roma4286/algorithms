from dataclasses import dataclass

@dataclass(eq=False)
class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None    

def create_bst(values: list[int]) -> TreeNode:
    root = TreeNode(val=values[0])

    for value in values:
        next_r = root
        while True:
            if value == next_r.val:
                break
            elif value < next_r.val:
                if next_r.left is None:
                    next_r.left = TreeNode(val=value)
                    break
                next_r = next_r.left
            else:
                if next_r.right is None:
                    next_r.right = TreeNode(val=value)
                    break
                next_r = next_r.right

    return root