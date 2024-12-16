# 3. Roman to Integer
# Sep 30, 2024
# Beats 14.98% Runtime
# Beats 95.81% Memory

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        lst = []

        for i in range ( len(s) ):
            # If greater, add the current value minus twice the most recent number
            if i > 0 and d[s[i]] > d[s[i - 1]]:
                lst.append( d[s[i]] - (2 * lst[len(lst) - 1]) )
            else: 
                lst.append( d[s[i]] )
        
        return sum(lst)
