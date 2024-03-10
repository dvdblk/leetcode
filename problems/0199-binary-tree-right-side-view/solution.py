from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # key = tree level, value = the value of the rightmost node in that level
        val_dict = dict()
        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()

            if node:
                val_dict[level] = node.val

                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

        vals = []
        for i in range(len(val_dict.keys())):
            vals.append(val_dict[i])

        return vals

    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        """BFS w/o hashmap"""
        result = []
        last_level = 0
        last_val = root.val if root is not None else None

        queue = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()

            if node is not None:
                # add last value to the result if a new level is reached
                if last_level < level:
                    result.append(last_val)
                last_level = level
                last_val = node.val

                queue.append((node.left, level+1))
                queue.append((node.right, level+1))

        # add the final last_val if needed
        if last_val is not None:
            result.append(last_val)

        return result

