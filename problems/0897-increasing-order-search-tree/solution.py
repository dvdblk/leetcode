# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """Two pass DFS inorder"""
        def dfs(node):
            if node is None:
                return []
            else:
                return dfs(node.left) + [node.val] + dfs(node.right)

        inorder = dfs(root)
        result = curr = TreeNode()
        for val in inorder:
            curr.right = TreeNode(val)
            curr = curr.right

        return result.right

    def increasingBST2(self, root: TreeNode) -> TreeNode:
        """Recursive DFS"""
        def dfs(node, tail):
            if node is None:
                return tail
            else:
                result = dfs(node.left, node)
                node.left = None
                node.right = dfs(node.right, tail)
                return result

        return dfs(root, None)