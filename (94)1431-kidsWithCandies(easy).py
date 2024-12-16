# 1431. Kids With the Greatest Number of Candies
# Sep 22, 2024
# Beats 5.29% Runtime
# Beats 33.94% Memory

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        greatest = max(candies)
        lst = []
        for kid in candies:
            if kid + extraCandies >= greatest:
                lst.append(True)
            else: 
                lst.append(False)
        return lst        
