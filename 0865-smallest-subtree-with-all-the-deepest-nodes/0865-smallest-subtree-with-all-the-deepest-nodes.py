# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root):
        
        def dfs(node):
            if not node:
                return (0, None)   # depth, subtree root
            
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            
            # Case 1: left subtree is deeper
            if left_depth > right_depth:
                return (left_depth + 1, left_node)
            
            # Case 2: right subtree is deeper
            if right_depth > left_depth:
                return (right_depth + 1, right_node)
            
            # Case 3: both are equal → this node is answer
            return (left_depth + 1, node)
        
        return dfs(root)[1]
