# 567. Permutation in String
# Oct 5, 2024
# Beats 21.85% Runtime
# Beats 75.44% Memory

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d = {}
        for ch in s1:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        
        for i in range( len(s2) - len(s1) + 1):
            sub = s2[ i : (i + len(s1)) ]
            d2 = {}
            for ch in sub:
                if ch in d2 and ch in d:
                    d2[ch] += 1
                elif ch in d:
                    d2[ch] = 1

            if len(d) == len(d2):
                if d == d2:
                    return True

        return False
