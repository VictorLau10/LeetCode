# 1071. Greatest Common Divisor of Strings
# Sep 17, 2024
# Beats 17.33% Runtime
# Beats 39.46% Memory

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str2) > len(str1):
            bigger = str2
            smaller = str1
        else:
            bigger = str1
            smaller = str2

        for i in range(1, len(smaller) + 1):
            splice = smaller[:len(smaller)//i]
            if splice * (len(bigger)//(len(smaller)//i)) == bigger and splice * i == smaller:
                return splice
        return ""
