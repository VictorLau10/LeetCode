# 179. Largest Number
# Sep 18, 2024
# Beats 5.24% Runtime
# Beats 69.36% Memory

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Optimizing the biggest numbers as early as you can
        # Ex. Between 9 and 89999999999999, placing the 9 first is always better.
        
        # Alg
        separatedDigits = []
        for num in nums:
            separatedDigits.append( list(str(num)) )
        separatedDigits.sort()

        # Compare between two numbers right next to each other, and see which combination is best
        i = 0
        while i in range( len(separatedDigits) - 1):
            while (separatedDigits[i] + separatedDigits[i + 1]) > (separatedDigits[i + 1] + separatedDigits[i]):
                separatedDigits[i], separatedDigits[i + 1] = separatedDigits[i + 1], separatedDigits[i]
                i = 0
            i += 1

        # Final concatenation
        s = ""
        for i in range(len(separatedDigits) - 1, -1, -1):
            for j in range( len(separatedDigits[i]) ):
                s += separatedDigits[i][j]

        if s[0] == '0':
            return '0'

        return s
