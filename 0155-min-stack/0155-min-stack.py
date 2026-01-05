class MinStack:

    def __init__(self):
        # Main stack to store all values
        self.stack = []
        
        # Auxiliary stack to store the minimum value at each level
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push value into the main stack
        self.stack.append(val)
        
        # If min_stack is empty, val is the minimum
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # Store the minimum between current value and previous minimum
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # Remove the top element from both stacks
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the current minimum element
        return self.min_stack[-1]
