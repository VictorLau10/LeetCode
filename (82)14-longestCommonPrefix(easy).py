# 14. Longest Common Prefix
# Oct 16, 2024
# Beats 7.35% Runtime
# Beats 40.87% Memory

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        smallest = strs[0]
        for string in strs:
            if len(string) < len(smallest):
                smallest = string

        res = ""
        for i in range(len(smallest)):
            ch = string[i]
            for string in strs:
                if len(string) == 0:
                    return ""
                if string[i] != ch:
                    return res
            res += ch

        return res     
        
        
