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
