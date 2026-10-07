# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertNode(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return node
        tmp = node.right
        node.right = self.invertNode(node.left)
        node.left = self.invertNode(tmp)

        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self.invertNode(root)
