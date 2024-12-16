# 3. Longest Substring without Repeating Characters
# Sep 29, 2024
# Beats 54.68% Runtime
# Beats 24.06% Memory

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Loop through array once
        # Keep track of all letters in current substring with dictionary
        # Keep track of the start of our current substring
        # Each letter will be the key to its index
        # Keep track of greatest number of elements in the dictionary at once
        # If any of those letters repeat, cut the substring so it starts right after 
        # the index of the repeated letter. 
        # Update the start of the current substring to right after that index and add it to a list.
        # At the end, find the max of that list.

        d = {}
        lst = [0]
        currentSubHead = 0

        for i in range ( len(s) ):
            if s[i] not in d:
                d[s[i]] = i
            else:
                lst.append(i - currentSubHead)
                if (d[s[i]] + 1) > currentSubHead:
                    currentSubHead = d[s[i]] + 1
                d[s[i]] = i
        lst.append( (len(s) - 1) - currentSubHead + 1)

        return max(lst) 
        
