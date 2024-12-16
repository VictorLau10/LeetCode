# Sep 16, 2024
# Beats 7.89% on Runtime
# Beats 9.07% on Memory

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        lst = []
        for i in range(len(timePoints)):
            hr = int(timePoints[i][:2])
            mi = int(timePoints[i][3:5])
            totalMin = hr * 60 + mi
            lst.append(totalMin)
        lst.sort()
        
        if lst[1] - lst[0] == 0:
            return 0
        
        simulator = lst[0]
        currentDiff = 0
        currentIndex = 1
        minDiff = 24 * 60
        for i in range ((24 * 60) + 1):
            if currentIndex < len(lst) - 2 and lst[currentIndex] == lst[currentIndex + 1]:
                return 0

            simulator += 1
            if simulator == 24*60:
                simulator = 0
            currentDiff += 1
            if currentIndex < len(lst) and simulator == lst[currentIndex]:
                if currentDiff < minDiff:
                    minDiff = currentDiff
                currentDiff = 0
                currentIndex += 1
        lastMin = lst[0] + (24 * 60) - lst[len(lst) - 1]
        
        if lastMin < minDiff:
            minDiff = lastMin
        return minDiff
                

        

        
        
