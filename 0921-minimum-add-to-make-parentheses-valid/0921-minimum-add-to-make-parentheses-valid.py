class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Approach 1

        # stack = []
        # count = 0

        # for i in s:
        #     if i == "(":
        #         stack.append(i)
        #     else:
        #         if stack:
        #             stack.pop()
        #         else:
        #             count += 1
        
        # count += len(stack)

        # return count

        # Approach 2
        
        add_count = 0
        remove_count = 0

        for i in s:
            if i == "(":
                add_count += 1
            else:
                if add_count > 0:
                    add_count -= 1
                else:
                    remove_count += 1

        return add_count + remove_count