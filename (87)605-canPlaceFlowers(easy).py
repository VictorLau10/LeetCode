# 605. Can Place Flowers
# Oct 3, 2024
# Beats 5.02% Runtime
# Beats 25.33% Memory

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Edge cases
        if len(flowerbed) <= 1 and flowerbed[0] == 0:
            return True
        if len(flowerbed) > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if len(flowerbed) - 2 >= 0 and flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
            flowerbed[len(flowerbed) - 1] = 1
            n -= 1

        for i in range ( 1, len(flowerbed) - 1 ):
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
        
        return n <= 0
