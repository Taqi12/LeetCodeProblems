class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        operations = []
        j = 0

        for i in range(1, n + 1):
            if j == len(target):
                break

            # Always push the current number      
            operations.append("Push")
            
            if i == target[j]:
                # this number is needed
                j += 1
            else:
                # this number is not needed
                operations.append("Pop")
        return operations
        