from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        current_level = 0
        last_value = root.val - 1
        queue = deque([(root, current_level)])

        while queue:
            node, level = queue.popleft()

            if node is not None:
                even_level = level % 2 == 0
                if level == current_level:
                    if (even_level and last_value >= node.val) or (
                        not even_level and last_value <= node.val
                    ):
                        return False

                last_value = node.val
                current_level = level

                if even_level and node.val % 2 == 0:
                    return False
                elif not even_level and node.val % 2 == 1:
                    return False

                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

        return True
