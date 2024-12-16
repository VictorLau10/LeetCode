# 2696. Minimum String Length After Removing Substrings
# Oct 7, 2024
# Beats 13.93% Runtime
# Beats 82.49% Memory

class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        front = 'AC'
        back = 'BD'

        # For every character in s
            # If stack is started
                # If character is in front
                    # add it to stack
                # If character is in back
                    # Pop from stack, make sure its same index
                # Else end the stack
            # Else if character is in front
                # Start the stack
        total = len(s)
        for ch in s:
            if len(stack) > 0:
                if ch in front:
                    stack.append(ch)
                elif ch in back:
                    elem = stack.pop()
                    if front.index(elem) == back.index(ch):
                        total -= 2
                    else:
                        stack = []
                else:
                    stack = []
            elif ch in front:
                stack.append(ch)
        
        return total
