# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # key = level
        # value = sum of values per node in that level, number of nodes
        values_per_level = {}

        # recursive DFS
        def helper(node, level):
            if node is not None:
                if elem := values_per_level.get(level):
                    values_per_level[level] = (elem[0] + node.val, elem[1] + 1)
                else:
                    values_per_level[level] = (node.val, 1)
                helper(node.left, level+1)
                helper(node.right, level+1)

        helper(root, 0)

        # create the averages from sums
        result = [0] * len(values_per_level.keys())
        for key, val in values_per_level.items():
            if not val[1]:
                result[key] = None
            else:
                result[key] = val[0]/val[1]

        return result