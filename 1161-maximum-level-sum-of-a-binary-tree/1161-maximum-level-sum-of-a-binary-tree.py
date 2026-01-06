class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = [root]
        index = 0

        level = 1
        max_sum = float('-inf')
        answer_level = 1

        while index < len(queue):
            level_size = len(queue) - index
            current_sum = 0

            for _ in range(level_size):
                node = queue[index]
                index += 1

                current_sum += node.val 

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)  # FIXED

            if current_sum > max_sum:
                max_sum = current_sum
                answer_level = level
            
            level += 1

        return answer_level
