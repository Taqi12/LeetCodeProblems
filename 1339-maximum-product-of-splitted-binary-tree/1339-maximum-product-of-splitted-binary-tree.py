# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        MOD = 10**9 + 7

        # Calculate total_sum
        def get_total_sum(node):
            if not node:
                return 0
            return node.val + get_total_sum(node.left) + get_total_sum(node.right)

        total_sum = get_total_sum(root)
        self.max_product = 0

        # DFS to calculate subtree sums and max_product

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            subtree_sum = node.val + left_sum + right_sum


            # Calculate the product by cutting above this subtree
            product = subtree_sum * (total_sum - subtree_sum)

            self.max_product = max(self.max_product, product)

            return subtree_sum

        dfs(root)

        return self.max_product % MOD
        