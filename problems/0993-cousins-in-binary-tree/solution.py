# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [(root, 0, None)]

        x_depth, x_parent, y_depth, y_parent = None, None, None, None

        while queue:
            node, depth, parent = queue.pop(0)

            if node:
                if node.val == x:
                    x_depth = depth
                    x_parent = parent

                    # early stopping optim
                    if y_depth is not None:
                        break
                elif node.val == y:
                    y_depth = depth
                    y_parent = parent

                    # early stopping optim
                    if x_depth is not None:
                        break

                queue.append((node.left, depth+1, node))
                queue.append((node.right, depth+1, node))

        return x_depth is not None and x_parent is not None and x_depth == y_depth and x_parent != y_parent