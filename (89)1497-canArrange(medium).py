# 1497. Check if Array Pairs are Divisible by k
# Oct 1, 2024
# Beats 5.28% Runtime
# Beats 10.71% Memory

class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for num in arr:
            remainder = num % k
            if remainder not in d: 
                d[remainder] = 1
            else:
                d[remainder] += 1

        # For each number, check if there is a number that can pair up with it,
        # then subtract 1 from both.
        print(d)
        for num in d:
            while (k - num) in d and d[k - num] > 0:
                if d[k - num] <= 0:
                    return False
                else:
                    d[num] -= 1
                    d[k - num] -= 1
        print(d)

        # Check that each key points to 0
        for num in d:
            if d[num] != 0 and num != 0:
                return False
        # Check for 0 in the dictionary, make sure it is even
        if 0 in d and d[0] % 2 != 0:
            return False
                                    
        return True
